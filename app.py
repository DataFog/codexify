from flask import Flask, request, jsonify, send_file, make_response, Response
from transformers import AutoTokenizer, AutoModelForTokenClassification
import io
from io import BytesIO, StringIO
import pandas as pd
from openpyxl import Workbook
from redaction_methods import redact_fixed_string, redact_random_value,redact_hash
import json
from more_itertools import chunked
from nerpii.named_entity_recognizer import NamedEntityRecognizer, split_name
from nerpii.faker_generator import FakerGenerator
from faker import Faker
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_NAME = "jorgeutd/bert-large-uncased-finetuned-ner"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)
# 
pii_keywords = ["account_number", "age", "date", "date_interval", "dob", "driver_license", "duration", "email_address", "event", "filename", "gender_sexuality", "healthcare_number", "ip_address", "language", "location", "location_address", "location_city", "location_coordinate", "location_country", "location_state", "location_zip", "marital_status", "money", "name", "name_family", "name_given", "numerical_pii", "organization", "occupation", "origin", "passport_number", "password", "phone_number", "physical_attribute", "political_affiliation", "religion", "ssn", "time", "url", "username", "vehicle_id", "zodiac_sign", "blood_type", "condition", "dose", "drug", "injury", "medical_process", "statistics", "bank_account", "credit_card", "credit_card_expiration", "cvv", "routing_number"]

# PII Detection Functions

def detect_pii(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(-1).squeeze().tolist()

    pii_detected = False
    for pred in predictions:
        if pred != 0:
            pii_detected = True
            break

    return pii_detected

def textform_pii_detect(text):
    max_seq_len = tokenizer.model_max_length - 2  # Account for special tokens [CLS] and [SEP]

    redacted_text = ""
    pii_detected = False

    # Split the text into smaller chunks if it exceeds the maximum sequence length
    text_chunks = chunked(tokenizer.tokenize(text), max_seq_len)

    for chunk in text_chunks:
        inputs = tokenizer(chunk, return_tensors="pt", is_split_into_words=True)
        outputs = model(**inputs)
        predictions = outputs.logits.argmax(-1).squeeze().tolist()

        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())

        for token, pred in zip(tokens, predictions):
            if pred != 0:
                pii_detected = True
                redacted_text += "REDACT "
            else:
                redacted_text += token + " "

    return pii_detected, redacted_text.strip()

def detect_pii_and_redact(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(-1).squeeze().tolist()

    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
    redacted_text = ""

    pii_detected = False
    for token, pred in zip(tokens, predictions):
        if pred != 0:
            pii_detected = True
            redacted_text += "REDACT "
        else:
            redacted_text += token + " "

    return pii_detected, redacted_text.strip()

def find_data_start_row(file, threshold=0.8):
    data = pd.read_excel(file, engine="openpyxl")
    file.seek(0)

    for index, row in data.iterrows():
        non_empty_cells = row.count()
        num_columns = len(row)
        if non_empty_cells / num_columns >= threshold:
            return index, num_columns

    return 0, data.shape[1]
  # Default to the first row if no suitable row is found


# Text Redaction Routes

# @app.route("/api/process_text", methods=["POST"])
# def api_process_text():
#     text = request.form.get("text")
#     redaction_method = request.form.get('redaction_method', 'fixed_string')

#     if not text:
#         return jsonify({"error": "Text is required"}), 400

#     pii_detected, redacted_text = textform_pii_detect(text)

#     # Return the redacted text as plain text
#     return Response(redacted_text, content_type='text/plain')

@app.route("/api/process_text", methods=["POST"])
def api_process_text():
    text = request.form.get("text")
    redaction_method = request.form.get('redaction_method', 'fixed_string')
    synthetic_data_generation = request.form.get('synthetic_data_generation', 'false')

    if not text:
        return jsonify({"error": "Text is required"}), 400

    if synthetic_data_generation.lower() == 'true':
        # Use NERPii to generate synthetic data.
        # recognizer = NamedEntityRecognizer(text)
        # recognizer.assign_entities_with_presidio(text)
        # recognizer.assign_entities_manually()
        # recognizer.assign_organization_entity_with_model()
        # synthetic_data = generator.get_faker_generation(text, recognizer.dict_global_entries)
        # return Response(synthetic_data, content_type='text/plain')
        return "Feature is under construction"
    else:
        pii_detected, redacted_text = textform_pii_detect(text)
        # Return the redacted text as plain text
        return Response(redacted_text, content_type='text/plain')



@app.route("/api/process_csv", methods=["POST"])
def api_process_csv():

    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(filename)
    redaction_method = request.form.get('redaction_method', 'fixed_string')
    synthetic_data_generation = request.form.get('synthetic_data_generation', 'false')
    temp_csv = io.BytesIO()

    if 'file' not in request.files:
        return jsonify({"error": "File is required"}), 400

    # load dataframe
    df = pd.read_csv(filename)
    
    # Read just the header row
    df_header = pd.read_csv(filename, nrows=0)
    name_columns = ['name', 'fullname', 'full_name', 'legal name', 'full legal name']  # you can customize this list based on your data

    # Check if there is a column that needs to be split into first and last names
    for column in df_header.columns:
        if column.lower() in name_columns:
            # Remember the index of the column
            # column_index = df.columns.get_loc(column)

            # Split the column into two columns
            df = split_name(df, column)

            # # Get the names of the new columns
            # first_name_column = 'first_name'
            # last_name_column = 'last_name'

            # # Remove the new columns from the end of the DataFrame
            # first_name = df[first_name_column]
            # last_name = df[last_name_column]
            # df = df.drop(columns=[first_name_column, last_name_column])

            # # Convert the DataFrame to a dictionary
            # df_dict = df.to_dict('list')

            # # Insert the new columns at the right position in the dictionary
            # df_dict = {key: df_dict[key] for key in list(df_dict.keys())[:column_index]} \
            #         + {first_name_column: first_name} \
            #         + {last_name_column: last_name} \
            #         + {key: df_dict[key] for key in list(df_dict.keys())[column_index:]}

            # # Convert the dictionary back to a DataFrame
            # df = pd.DataFrame(df_dict)

            break

    if synthetic_data_generation.lower() == 'true':
        
        recognizer = NamedEntityRecognizer(df)
        recognizer.assign_entities_with_presidio()
        recognizer.assign_entities_manually()
        recognizer.assign_organization_entity_with_model()
        # print(recognizer.dict_global_entities)

        generator = FakerGenerator(df,recognizer.dict_global_entities) 
        generator.get_faker_generation()
        
        df = generator.dataset
        df.to_csv(temp_csv, mode='ab', index=False, header=True, lineterminator='\n')


        temp_csv.seek(0)
        response = make_response(send_file(temp_csv, download_name='redacted_output.csv', mimetype='text/csv', as_attachment=True))
        response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.csv'
        os.remove(filename)
        return response

    else:
        # Read only the header row
        header_row = pd.read_csv(file, nrows=0)
        header_redact_flags = []

        # Scan the header row to see if the description matches a PII category
        for column in header_row.columns:
            column_str = str(column).lower()
            contains_pii_keyword = any(keyword in column_str for keyword in pii_keywords)
            header_redact_flags.append(detect_pii(column_str) or contains_pii_keyword)
        print(header_redact_flags)
        
        # Define a function to apply redaction based on header flags
        def redact_by_header_flags(row, method):
            redaction_func = {
                'fixed_string': redact_fixed_string,
                'random_value': redact_random_value,
                'hash': redact_hash,
                # Add more methods as needed
            }.get(method, redact_fixed_string)

            for index, value in enumerate(row):
                if header_redact_flags[index]:
                    row[index] = redaction_func(value)
            return row

        # Write the header row to the output CSV
        header_row.to_csv(temp_csv, mode='w', index=False, lineterminator='\n')

        # Process the CSV in chunks, redacting the data as needed
        chunksize = 1000
        file.seek(0)
        for chunk in pd.read_csv(file, chunksize=chunksize, header=None, names=header_row.columns, skiprows=1):
            chunk = chunk.apply(lambda row: redact_by_header_flags(row, redaction_method), axis=1)
            chunk.to_csv(temp_csv, mode='ab', index=False, header=False, lineterminator='\n')

        temp_csv.seek(0)
        response = make_response(send_file(temp_csv, download_name='redacted_output.csv', mimetype='text/csv', as_attachment=True))
        response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.csv'
        return response


@app.route("/api/process_excel", methods=["POST"])
def api_process_excel():
    
    if 'file' not in request.files:
        return jsonify({"error": "File is required"}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(filename)
    redaction_method = request.form.get('redaction_method', 'fixed_string')
    temp_excel = io.BytesIO()
    synthetic_data_generation = request.form.get('synthetic_data_generation', 'false')

    data_start_row, num_columns = find_data_start_row(file)

    # load dataframe
    df = pd.read_excel(filename)
    
    # Read just the header row
    df_header = pd.read_excel(filename, nrows=0)
    name_columns = ['name', 'fullname', 'full_name', 'legal name', 'full legal name']  # you can customize this list based on your data


    if synthetic_data_generation.lower() == 'true':
        recognizer = NamedEntityRecognizer(df)
        recognizer.assign_entities_with_presidio()
        recognizer.assign_entities_manually()
        recognizer.assign_organization_entity_with_model()
        # print(recognizer.dict_global_entities)

        generator = FakerGenerator(df,recognizer.dict_global_entities) 
        generator.get_faker_generation()
        
        df = generator.dataset
        df.to_csv(temp_excel, mode='ab', index=False, header=True, lineterminator='\n')


        temp_excel.seek(0)
        response = make_response(send_file(temp_excel, download_name='redacted_output.csv', mimetype='text/csv', as_attachment=True))
        response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.csv'
        os.remove(filename)
        return response



    else:
        # Read only the header row
        header_row = pd.read_excel(file, nrows=0, usecols=range(num_columns))

        header_redact_flags = []

        # Scan the header row to see if the description matches a PII category
        for column in header_row.columns:
            column_str = str(column).lower()
            contains_pii_keyword = any(keyword in column_str for keyword in pii_keywords)
            header_redact_flags.append(detect_pii(column_str) or contains_pii_keyword)

        # Define a function to apply redaction based on header flags
        def redact_by_header_flags(row, method):
            redaction_func = {
                'fixed_string': redact_fixed_string,
                'random_value': redact_random_value,
                'hash': redact_hash,
                # Add more methods as needed
            }.get(method, redact_fixed_string)

            for index, value in enumerate(row):
                if header_redact_flags[index]:
                    row[index] = redaction_func(value)
            return row


        # Write the header row to the output Excel
        output_book = Workbook()
        output_sheet = output_book.active
        output_sheet.append(header_row.columns.tolist())


        # Process the Excel file in chunks, redacting the data as needed
        chunksize = 1000
        file.seek(0)
        header_rows_to_skip = 1

        num_rows = pd.read_excel(file, engine="openpyxl").shape[0]
        file.seek(0)

        for start_row in range(header_rows_to_skip, num_rows, chunksize):
            chunk = pd.read_excel(
                file, engine="openpyxl", skiprows=data_start_row, nrows=chunksize, header=None, usecols=range(num_columns)
            )

            chunk.columns = header_row.columns
            chunk = chunk.apply(lambda row: redact_by_header_flags(row, redaction_method), axis=1)
            for _, row in chunk.iterrows():
                output_sheet.append(row.tolist())


        output_book.save(temp_excel)
        temp_excel.seek(0)
        response = make_response(send_file(temp_excel, download_name='redacted_output.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', as_attachment=True))
        response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.xlsx'
        return response

@app.route("/api/process_json", methods=["POST"])
def api_process_json():
    if 'file' not in request.files:
        return jsonify({"error": "File is required"}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(filename)
    redaction_method = request.form.get('redaction_method', 'fixed_string')
    synthetic_data_generation = request.form.get('synthetic_data_generation', 'false')
    temp_json = io.BytesIO()

    # Read the JSON file
    data = pd.read_json(filename)
    file.seek(0)

    if synthetic_data_generation.lower() == 'true':
        # def json_synthetic_data_add(data_dict):


        #     for key, value in data_dict.items():
        #         if isinstance(value, dict):
        #             json_synthetic_data_add(value)
        #         elif isinstance(value, list):
        #             for index, item in enumerate(item):
        #                 if isinstance(item, dict):
        #                     json_synthetic_data_add(data_dict)
        #                 else:
        #                     item_str = str(item)
        #                     if detect_pii(item_str) or any(keyword in item_str.lower() for keyword in pii_keywords):
        #                         value[index] = redaction_func(item_str)
        #         else:
        #             value_str = str(value)
        #             recognizer = NamedEntityRecognizer(value_str)
        #             recognizer.assign_entities_with_presidio()
        #             recognizer.assign_entities_manually()
        #             recognizer.assign_organization_entity_with_model()

        #             generator = FakerGenerator(data,recognizer.dict_global_entities) 
        #             generator.get_faker_generation()
                    
        #             data = generator.dataset
        #             value[index] = redaction_func(value_str)

        #     return data_dict

        # # Process and redact the data using the existing synthetic data logic
        # data_dict = json.loads(file.read())
        # synthetic_json = json_synthetic_data_add(data_dict)


        # # Write the redacted data back to a JSON file
        # temp_json.write(json.dumps(synthetic_json).encode())
        # # temp_json.write(data.to_json(orient='records').encode())


        # temp_json.seek(0)

        # response = make_response(send_file(temp_json, download_name='redacted_output.json', mimetype='application/json', as_attachment=True))
        # response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.json'
        # return response
        return "This feature is under construction."

    else:
        # Define a function to apply redaction based on header flags
        def redact_by_header_flags(data_dict, method):
            redaction_func = {
                'fixed_string': redact_fixed_string,
                'random_value': redact_random_value,
                'hash': redact_hash,
                # Add more methods as needed
            }.get(method, redact_fixed_string)

            for key, value in data_dict.items():
                if isinstance(value, dict):
                    redact_by_header_flags(value, method)
                elif isinstance(value, list):
                    for index, item in enumerate(value):
                        if isinstance(item, dict):
                            redact_by_header_flags(item, method)
                        else:
                            item_str = str(item)
                            if detect_pii(item_str) or any(keyword in item_str.lower() for keyword in pii_keywords):
                                value[index] = redaction_func(item_str)
                else:
                    value_str = str(value)
                    if detect_pii(value_str) or any(keyword in value_str.lower() for keyword in pii_keywords):
                        data_dict[key] = redaction_func(value_str)

            return data_dict

        # Process and redact the data using the existing redaction logic
        data_dict = json.loads(file.read())
        redacted_data = redact_by_header_flags(data_dict, redaction_method)


        # Write the redacted data back to a JSON file
        temp_json.write(json.dumps(redacted_data).encode())

        temp_json.seek(0)

        response = make_response(send_file(temp_json, download_name='redacted_output.json', mimetype='application/json', as_attachment=True))
        response.headers['Content-Disposition'] = 'attachment; filename=redacted_output.json'
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=6000)
