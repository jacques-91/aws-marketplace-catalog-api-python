class scan_request:
    def __init__(self, session):
        self.client = session.client('marketplace-catalog')

    def start_scan(self, product_id, instance_type, ami_id, access_role, username, port, operating_system, operating_version):
        
        change_set_request = [
            {
                "ChangeType": "AddDeliveryOptions",
                "Entity": {
                    "Type": "AmiProduct@1.0",
                    "Identifier": product_id
                },
                "DetailsDocument": {
                    "Version": {
                        "VersionTitle": "Scan Validation",
                        "ReleaseNotes": "This is just for a scanning event"
                    },
                    "DeliveryOptions": [
                        {
                            "Details": {
                                "AmiDeliveryOptionDetails": {
                                    "UsageInstructions": "Not application for scanning",
                                    "RecommendedInstanceType": instance_type,
                                    "SecurityGroups": [
                                        {
                                            "IpProtocol": "tcp",
                                            "FromPort": int(port),
                                            "ToPort": int(port),
                                            "IpRanges": [
                                                "0.0.0.0/0"
                                            ]
                                        }
                                    ],
                                    "AmiSource": {
                                        "AmiId": ami_id,
                                        "AccessRoleArn": access_role,
                                        "Username": username,
                                        "ScanningPort": int(port),
                                        "OperatingSystemName": operating_system,
                                        "OperatingSystemVersion": operating_version
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
        
        try:
            response = self.client.start_change_set(
                Catalog='AWSMarketplace',
                ChangeSet=change_set_request,
                Intent='VALIDATE'
            )
            return response
        except Exception as e:
            print(f"Validation Request Failed: {e}")
            raise
