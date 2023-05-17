
# PII Detection
curl -X POST -H "Content-Type: application/json" -d '{"text": "My name is John Doe, and my email is john.doe@example.com"}' http://127.0.0.1:5000/api/detect_pii

# CSV Detection
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/titanic.csv" -F "redaction_method=hash" http://127.0.0.1:5000/api/process_csv --output redacted_output.csv

curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/titanic.csv" -F "synthetic_data_generation=true" http://127.0.0.1:5000/api/process_csv --output redacted_output.csv


# Excel Detection
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/path/to/your_excel_file.xlsx" "<your_server_url>/api/process_excel" --output redacted_output.xlsx

curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Downloads/activity.xlsx" "http://127.0.0.1:5000/api/process_excel" --output redacted_output.xlsx

curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Downloads/titanic.xlsx" -F "redaction_method=hash" "http://127.0.0.1:5000/api/process_excel" --output redacted_output.xlsx

Date	Description	Card Member	Account #	Amount
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	6.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	6.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	6.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	6.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	SIDDHARTH MOHAN	-91005	6.95

Date	Description	Card Member	Account #	Amount
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95
08/20/2022	AplPay VEEROTECH * VCLAYTON             NC	REDACT REDACT	-REDACT	5.95

# JSON Detection
pii_fields.json
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/sample.json" -F "redaction_method=hash" http://localhost:5000/api/process_json -o redacted_output.json


sudo /Users/sidmohan/.pyenv/versions/3.10.5/bin/python3.10 -m pip freeze > requirements.txt


# text synthetic 
curl -X POST -F "text="My name is John Doe, and my email is john.doe@example.com"" -F "synthetic_data_generation=true" http://localhost:6000/api/process_text


# csv synthetic
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/titanic_short.csv" -F "synthetic_data_generation=true" http://127.0.0.1:6000/api/process_csv --output redacted_output.csv

curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/PersonalInfo.csv" -F "synthetic_data_generation=true" http://127.0.0.1:6000/api/process_csv --output redacted_output.csv


# excel synthetic
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/PersonalInfo.xlsx" "http://127.0.0.1:6000/api/process_excel" -F "synthetic_data_generation=true" --output redacted_output.xlsx


# json synthetic
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/sidmohan/Desktop/codexify/api/samples/sample.json" -F "synthetic_data_generation=true" http://localhost:6000/api/process_json -o redacted_output.json