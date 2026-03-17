import boto3

aws_session = boto3.Session

aws_credentials = aws_session.get_credentials()

if aws_credentials
	aws_access_key = aws_credentials.access_key
	aws_secret_key = aws_credentials.secret_key
	aws_session_token = aws_credentials.token
else
	print("AWS Credentials required.")
