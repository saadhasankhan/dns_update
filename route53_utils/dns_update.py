"""

Created on June 28, 2019

@author: skhan

"""
import argparse
import boto3


def main():
    # Argument handling
    parser=argparse.ArgumentParser(description='Change records in route53/ops.cloud.cengage.com')
    required_args = parser.add_argument_group('required named arguments')
    optional_args = parser.add_argument_group('optional named arguments')
    required_args.add_argument('-e', '--environment', type=str, help='Enter AWS Profile', required=True)
    required_args.add_argument('-n', '--name', type=str, help='Record name', required=True)
    required_args.add_argument('-v', '--value', type=str, help='Record value, IP for A records, a host FQDN for CNAME', required=True)
    required_args.add_argument('-a', '--action', choices=['CREATE', 'DELETE', 'UPSERT'], type=str, help='Create, Update or Delete', required=True)
    required_args.add_argument('-t', '--type', type=str, choices=['A', 'CNAME'], default=2, help='A or CNAME', required=True)
    optional_args.add_argument('--TTL', type=int, default=300, required=False)
    required_args = parser.parse_args()
    optional_args = parser.parse_args()

    HostedZoneId = "Z10N775N1B7JYL"  # ops.cloud.cengage.com

    session = boto3.Session(profile_name=required_args.environment)
    client = session.client('route53')

    response = client.change_resource_record_sets(
        HostedZoneId=HostedZoneId,
        ChangeBatch={
            'Changes': [
                {
                    'Action': required_args.action,
                    'ResourceRecordSet': {
                        'Name': required_args.name,
                        'Type': required_args.type,
                        'TTL': optional_args.TTL,
                        'ResourceRecords': [
                            {
                                'Value': required_args.value
                            },
                        ],
                    }
                },
            ]
        })

    print(response)

if __name__ == '__main__':
    main()