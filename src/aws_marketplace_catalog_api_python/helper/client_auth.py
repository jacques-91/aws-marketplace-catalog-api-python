import boto3
import os
from botocore.exceptions import ProfileNotFound, NoCredentialsError

def get_aws_credential_session(access_key=None, secret_key=None, session_token=None, profile=None, credential_path=None):
	if credential_path:
		cred_path = os.path.abspath(os.path.expanduser(credential_path))
		os.environ['AWS_SHARED_CREDENTIALS_FILE'] = cred_path
	
	try:
		aws_session = boto3.Session(
			aws_access_key_id=access_key,
			aws_secret_access_key=secret_key,
			aws_session_token=session_token,
			profile_name=profile
		)

		aws_credentials = aws_session.get_credentials()
		if not aws_credentials:
			raise NoCredentialsError()

		print(f"AWS credentials successful [Method: {aws_credentials.method}]")
	
		return aws_session
	
	except ProfileNotFound:
		print("")
	except NoCredentialsError:
		print()
	except Exception as e:
		print()
	
	return None