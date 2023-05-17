
# WIP
import csv
import random
from faker import Faker
import faker.providers
from faker.providers import address, automotive, bank, barcode, color, company, credit_card, currency, date_time, emoji, file, geo, internet, isbn, job, lorem, misc, person, phone_number, profile, python, sbn, ssn, user_agent



# 24 standard providers
standard_providers = [
    address.Provider,
    automotive.Provider,
    bank.Provider,
    barcode.Provider,
    color.Provider,
    company.Provider,
    credit_card.Provider,
    currency.Provider,
    date_time.Provider,
    emoji.Provider,
    file.Provider,
    geo.Provider,
    internet.Provider,
    isbn.Provider,
    job.Provider,
    lorem.Provider,
    misc.Provider,
    person.Provider,
    phone_number.Provider,
    profile.Provider,
    python.Provider,
    sbn.Provider,
    ssn.Provider,
    user_agent.Provider ]
   


fake = Faker()

# pii_to_faker = {}

# for provider in standard_providers:
#     # Instantiate the provider
#     provider_instance = provider(fake)

#     # Loop over all methods of the provider
#     for method_name in dir(provider_instance):
#         # Ignore special methods (those that start with '__')
#         if not method_name.startswith('__'):
#             method = getattr(provider_instance, method_name)

#             # Check if the method is callable
#             if callable(method):
#                 # Add the method to pii_to_faker
#                 pii_to_faker[method_name] = method

pii_to_faker = {
# "animal_image": fake.animal_image(),
"ascii_company_email": fake.ascii_company_email(),
"ascii_email": fake.ascii_email(),
"ascii_free_email": fake.ascii_free_email(),
"ascii_safe_email": fake.ascii_safe_email(),
"boolean": fake.boolean(),
"building_number": fake.building_number(),
# "building_string": fake.building_string(),
"city": fake.city(),
# "city_name": fake.city_name(),
"city_prefix": fake.city_prefix(),
"city_suffix": fake.city_suffix(),
"color": fake.color(),
"company": fake.company(),
"company_email": fake.company_email(),
"coordinate": fake.coordinate(),
"country": fake.country(),
"country_calling_code": fake.country_calling_code(),
"credit_card_expire": fake.credit_card_expire(),
"credit_card_full": fake.credit_card_full(),
"credit_card_number": fake.credit_card_number(),
"credit_card_provider": fake.credit_card_provider(),
"credit_card_security_code": fake.credit_card_security_code(),
"currency": fake.currency(),
"currency_code": fake.currency_code(),
"date": fake.date(),
"date_between": fake.date_between(),
"date_between_dates": fake.date_between_dates(),
"date_object": fake.date_object(),
"date_of_birth": fake.date_of_birth(),
"day_of_month": fake.day_of_month(),
"day_of_week": fake.day_of_week(),
"domain_name": fake.domain_name(),
"domain_word": fake.domain_word(),
"dsv": fake.dsv(),
"ean": fake.ean(),
"email": fake.email(),
"file_extension": fake.file_extension(),
"file_name": fake.file_name(),
"file_path": fake.file_path(),
"first_name": fake.first_name(),
"first_name_female": fake.first_name_female(),
"first_name_male": fake.first_name_male(),
"first_name_nonbinary": fake.first_name_nonbinary(),
"fixed_width": fake.fixed_width(),
# "format": fake.format(),
"free_email": fake.free_email(),
"free_email_domain": fake.free_email_domain(),
# "geo_coordinate": fake.geo_coordinate(),
"hex_color": fake.hex_color(),
"image_url": fake.image_url(),
"internet_explorer": fake.internet_explorer(),
"ipv4": fake.ipv4(),
"ipv4_network_class": fake.ipv4_network_class(),
"ipv4_private": fake.ipv4_private(),
"ipv4_public": fake.ipv4_public(),
"ipv6": fake.ipv6(),
"isbn10": fake.isbn10(),
"isbn13": fake.isbn13(),
"job": fake.job(),
"language_code": fake.language_code(),
"language_name": fake.language_name(),
"last_name": fake.last_name(),
"last_name_female": fake.last_name_female(),
"last_name_male": fake.last_name_male(),
"last_name_nonbinary": fake.last_name_nonbinary(),
"latitude": fake.latitude(),
"latlng": fake.latlng(),
"license_plate": fake.license_plate(),
"linux_platform_token": fake.linux_platform_token(),
"linux_processor": fake.linux_processor(),
"locale": fake.locale(),
"longitude": fake.longitude(),
"mac_address": fake.mac_address(),
"mac_platform_token": fake.mac_platform_token(),
"mac_processor": fake.mac_processor(),
"md5": fake.md5(),
"msisdn": fake.msisdn(),
"name": fake.name(),
"name_female": fake.name_female(),
"name_male": fake.name_male(),
"name_nonbinary": fake.name_nonbinary(),
"nic_handle": fake.nic_handle(),
"nic_handles": fake.nic_handles(),
"null_boolean": fake.null_boolean(),
"opera": fake.opera(),
"paragraph": fake.paragraph(),
"paragraphs": fake.paragraphs(),
"password": fake.password(),
"phone_number": fake.phone_number(),
"postalcode": fake.postalcode(),
"prefix": fake.prefix(),
"prefix_female": fake.prefix_female(),
"prefix_male": fake.prefix_male(),
"prefix_nonbinary": fake.prefix_nonbinary(),
"profile": fake.profile(),
"pybool": fake.pybool(),
"pydecimal": fake.pydecimal(),
"pydict": fake.pydict(),
"pyfloat": fake.pyfloat(),
"pyint": fake.pyint(),
"pyiterable": fake.pyiterable(),
"pylist": fake.pylist(),
"pyobject": fake.pyobject(),
"pyset": fake.pyset(),
"pystr": fake.pystr(),
"pystr_format": fake.pystr_format(),
"pystruct": fake.pystruct(),
"pytuple": fake.pytuple(),
# "random": fake.random(),
"random_digit": fake.random_digit(),
"random_digit_not_null": fake.random_digit_not_null(),
"random_digit_or_empty": fake.random_digit_or_empty(),
"random_element": fake.random_element(),
"random_int": fake.random_int(),
"random_letter": fake.random_letter(),
"random_number": fake.random_number(),
"random_sample": fake.random_sample(),
"randomize_nb_elements": fake.randomize_nb_elements(),
# "rgba_color": fake.rgba_color(),
"safe_color_name": fake.safe_color_name(),
"safe_domain_name": fake.safe_domain_name(),
"safe_email": fake.safe_email(),
"safari": fake.safari(),
"sentence": fake.sentence(),
"sentences": fake.sentences(),
"sha1": fake.sha1(),
"sha256": fake.sha256(),
"slug": fake.slug(),
"ssn": fake.ssn(),
"street_address": fake.street_address(),
"street_name": fake.street_name(),
"street_suffix": fake.street_suffix(),
"suffix": fake.suffix(),
"suffix_female": fake.suffix_female(),
"suffix_male": fake.suffix_male(),
"suffix_nonbinary": fake.suffix_nonbinary(),
"tar": fake.tar(),
"text": fake.text(),
"texts": fake.texts(),
"time": fake.time(),
"time_delta": fake.time_delta(),
"time_object": fake.time_object(),
"timezone": fake.timezone(),
"tld": fake.tld(),
"tsv": fake.tsv(),
"unix_device": fake.unix_device(),
"unix_partition": fake.unix_partition(),
"uri": fake.uri(),
"uri_extension": fake.uri_extension(),
"uri_page": fake.uri_page(),
"uri_path": fake.uri_path(),
"url": fake.url(),
"user_agent": fake.user_agent(),
"uuid4": fake.uuid4(),
"windows_platform_token": fake.windows_platform_token(),
"word": fake.word(),
"words": fake.words(),
"zip": fake.zip()
}

# generate a dataset of 1000 rows for 



# Save the synthetic dataset to a CSV file
with open('synthetic_dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dataset)
