# Codexify: Identify, Mask, & Replace Personally Identifying Information (PII)

[![Official Website](https://img.shields.io/badge/Official%20Website-codexify.ai-blue?style=flat&logo=world&logoColor=white)](https://codexify.ai)
[![Slack](https://img.shields.io/badge/slack--channel-blue?logo=slack)](https://join.slack.com/t/codexifyworkspace/shared_invite/zt-1vbs0sulv-aNxrDCQVeCuFqIMSboIboA)

![Logo](https://uploads-ssl.webflow.com/63c04c507596187087b1cfa6/6447f61405d27dfc1f67d300_Color%20logo%20-%20no%20background-p-800.png)

<hr/>

### 🔴 THIS PRODUCT IS UNDERGOING REGULAR UPDATES: PLEASE CHECK BELOW FOR LATEST UPDATES  🔴

<hr/>
## Changelog
5/17/23: Added notes in wiki
5/16/23: Initial commit

## About

Data privacy and security are top priorities for any organization that deals with sensitive data. 

Codexify's API provides an easy-to-use solution for data stakeholders to redact sensitive data from CSV, Excel, and JSON files. Our API supports a range of redaction methods, including fixed string, random value, and hash functions, to ensure that sensitive data is removed from the files, while preserving the integrity of the remaining data.

In addition to redaction, Codexify's API also supports synthetic data generation to replace sensitive data with realistic but fake data. This feature can be useful when the sensitive data is needed for testing or development purposes, but cannot be used in its original form due to privacy concerns.

## Use Cases
### Data Analytics/ETL
Data analytics professionals working with ETL (Extract, Transform, Load) processes can find Codexify's API useful for redacting sensitive data from CSV, Excel, and JSON files. The API can help ensure that the data is compliant with data protection regulations and that sensitive data is not accidentally or intentionally included in reports or analyses.

Furthermore, the API's support for synthetic data generation can be useful for testing and development purposes, allowing data analytics professionals to work with realistic but safe data. Overall, Codexify's API is a flexible and customizable solution for data redaction that can be tailored to meet the specific needs of each organization and industry.

### Medical Records/Research
Codexify can be used to remove personally identifiable information (PII) from medical records and research data, such as patient names, social security numbers, and more, to protect patient privacy and comply with data protection regulations.

### Financial Documents
An important use case for data engineers using Codexify's API is within the context of financial organizations that deal with large volumes of sensitive data. The API can be used to redact PII from financial statements and other documents that may contain sensitive information, such as social security numbers, credit card numbers, and bank account details. This can help to reduce the risk of data breaches and ensure compliance with data protection regulations.

### Legal Briefs
Codexify can also be used in legal organizations to redact sensitive information from legal documents, such as contracts, agreements, and court filings. This can help to protect the privacy of individuals involved in legal proceedings and prevent sensitive information from being disclosed publicly.

## Platforms
* API (Locally hosted): download a Docker image and host Codexify on-premise - perfect for users that have rigorous data storage requirements.
* SaaS: Our API can also be accessible through a user-friendly interface [here](https://codexify.ai).
* Managed Services: We offer a range of paid custom services around helping you get up and running quickly. Please get in touch at sid@codexify.app to schedule a consultation. 
* Hosted Services: Depending on your organization needs, having Codexify live on GCP, AWS, DigitalOcean (and more) might make the most sense.  We offer a range of hosted plans that take care of all of the setup and installation. Contact sid@codexify.app for more information. 


## 🚀 Features

* Identify common PII fields in CSVs and other structured data
* Anonymize, hash, or redact your sensitive data
* Generate synthetic data variants and swap them in place of actual damaging information

### Coming up
* Enhancing support for detecting and generating *100+* types of synthetic data(!!)
* Support for larger file types
* HDFS support 
* Differential Privacy controls
* Data connectors  
* Are we missing anything? Please get in touch! 

## Quickstart
We're adding new content daily to help you get set up! If you have questions in the meantime, please feel free to reach out to us on Slack and/or email (sid@codexify.app)

0. Check out the [Open API specs](openapi.yaml)
1. Download the latest [Docker image](Dockerfile)
2. Read the [API documentation] (https://github.com/CodexifyAI/codexify/wiki/API-Reference)
3. Follow the [installation instructions](https://github.com/CodexifyAI/codexify/wiki/Installation-(via-Docker)-Instructions) to host or configure your private instance
4. Fire up the instance and start protecting your data!


## 🛡 Disclaimer

Please check out the terms of our [license](LICENSE.MD) for more information

## 💁 Connect with Us on Slack

We've started a new Slack channel to discuss best practices, feature requests, and address any questions you may have.  Join [here](https://join.slack.com/t/codexifyworkspace/shared_invite/zt-1vbs0sulv-aNxrDCQVeCuFqIMSboIboA)


We look forward to connecting with you and hearing your thoughts, ideas, and experiences with Codexify. If you would like to contribute to this effort or join our team, please get in touch! 

