\# AWS Cloud Resume Challenge



!\[AWS](https://img.shields.io/badge/AWS-Cloud-orange)

!\[Python](https://img.shields.io/badge/Python-3.14-blue)

!\[AWS SAM](https://img.shields.io/badge/AWS-SAM-Serverless-orange)

!\[DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-blue)

!\[Lambda](https://img.shields.io/badge/AWS-Lambda-orange)



\## Overview



This project is my implementation of the AWS Cloud Resume Challenge.



The project combines a static cloud-hosted resume website with a serverless visitor counter backend built using AWS Lambda and Amazon DynamoDB.



\### Live Resume



\*\*https://musaresume.bluetechnology.co.za\*\*



\## Architecture



```text

&#x20;                        ┌─────────────────────┐

&#x20;                        │       Visitor       │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │      Route 53       │

&#x20;                        │     DNS / Domain    │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │     CloudFront      │

&#x20;                        │   CDN / HTTPS / TLS │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │     Amazon S3       │

&#x20;                        │   Static Website    │

&#x20;                        └─────────────────────┘





&#x20;                    Visitor Counter

&#x20;                           │

&#x20;                           ▼

&#x20;                 ┌─────────────────────┐

&#x20;                 │   Lambda Function   │

&#x20;                 │    Function URL     │

&#x20;                 └──────────┬──────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                 ┌─────────────────────┐

&#x20;                 │      DynamoDB       │

&#x20;                 │   ResumeViewCount   │

&#x20;                 └─────────────────────┘

