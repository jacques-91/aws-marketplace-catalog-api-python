# aws-marketplace-catalog-api-python
Python based repository for using AWS Marketplace Catalog API

Disclaimer: I still need to setup tests, and all that, this is just the initial setup. (I'll also need to double tap and ensure it all works)

## Prerequisites

1. Python: https://www.python.org/downloads/ use Python3
2. Setup dedicated virtual env on your machine to avoid conflict with global python usage:
```
$ python -m venv .venv
...
$ source .venv/bin/activate
```
3. Install the boto3 client of AWS: `pip install boto3`


## Usage information

### Setting up your AWS Credentials

1. Manual credential input: Pass --access_key, --secret_key, and optionally the --session_token as arguments.
<br>Example: `python main.py --access_key xxx --secret_key xxx --session_token xxx`
2. Profile usage: Use the --profile to use a specific profile from your AWS Credentials configurations.
<br>Example: `python main.py --profile xxx`
3. Custom Credential file: When you have a custom file with credentials in it, use the --creds_file to point to the path for credentials.
<br>Example: `python main.py --creds_file /somepath/file`
4. Environment Variables: If you have already set/export credentials i.e. your default creds, no need to pass anything.

### Create your product (Server base AMI)

<Placeholder>

### Initiating a scan activity (Server base AMI)

*You **MUST** have an AWS Marketplace AMI Product already*

To perform the scan request / validation request (Also weirdly known as "Test Add Version" at least in the API it make sense)

pass the request as: `python -m aws_marketplace_catalog_api_python.main [authentication method] --product_id prod-xxx --ami_id ami-xxxxxxxx --access_role arn:aws:iam::xxxxxxx:role/xxxxx --username ec2-user --port 22 --operating_system AmazonLinux --operating_version 2023.x.x`

Required Inputs:
- product_id: Your listing product id.
- instance_type: Your recommended instance type that works well with your build. (Best launch scenario)
- ami_id: The AMI that you want to scan
- access_role: The role that allows access to the AMI
- username: The username to login to your AMI when the instance is spun up
- port: The specific port that is required to access the instance 

### Add Version (Server base AMI)

<Placeholder>

### Change metadata (listing information for server base AMI)

<Placeholder>
