import argparse
from aws_marketplace_catalog_api_python import get_aws_credential_session, scan_request

def aws_credentials_setup(input_parser):
	auth_group_input = input_parser.add_argument_group('Authentication')
	auth_group_input.add_argument('--access_key', help="AWS Access Key")
	auth_group_input.add_argument('--secret_key', help="AWS Secret Key")
	auth_group_input.add_argument('--session_token', help="AWS Session Token")
	auth_group_input.add_argument('--profile', help="AWS Profile")
	auth_group_input.add_argument('--creds_file', help="Custom credentials file path")

def scan_request_setup(input_parser):
	scanning_group = input_parser.add_argument_group('AMI Scan Parameters')
	scanning_group.add_argument('--product_id', help="The product id that you want to scan against", required=True)
	scanning_group.add_argument('--instance_type', help="The instance type that work best with your build", required=True)
	scanning_group.add_argument('--ami_id', help="AMI ID that will be scanned", required=True)
	scanning_group.add_argument('--access_role', help="Access Role ARN for scanning of AMI", required=True)
	scanning_group.add_argument('--username', help="Username for login", required=True)
	scanning_group.add_argument('--port', help="Access port for login", type=int, default=22, required=True)
	scanning_group.add_argument('--operating_system', help="Operating System of build", default="Amazon Linux"
	scanning_group.add_argument('--operating_version', help="Operating System Version", default="Latest")

def main():
	input_parser = argparse.ArgumentParser(description="AWS Marketplace requests")

	aws_credentials_setup(input_parser)
	scan_request_setup(inpute_parser)

	input_args = input_parser.parse_args()

	# Will most likely need to change, and revisit. For now initial request input.

	try:
		aws_session = get_aws_credential_session(
			access_key=input_args.access_key,
			secret_key=input_args.secret_key,
			session_token=input_args.session_token,
			profile=input_args.profile,
			credential_path=input_args.creds_file
		)

		request_scan = scan_request(aws_session)
		response = request_scan.start_scan(
			product_id=input_args.product_id,
			instance_type=input_args.instance_type,
			ami_id=input_args.ami_id,
			access_role=input_args.access_role,
			username=input_args.username,
			port=input_args.port,
			operating_system=input_args.operating_system,
			operating_version=input_args.operating_version
        )

		print(f"Scan Request Initaited ChangeSet: {response.get('ChangeSetId')}")
	
	except Exception as e:
		print(f"[ERROR] -- {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
