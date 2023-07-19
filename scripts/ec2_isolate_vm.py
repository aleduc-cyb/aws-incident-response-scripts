import boto3
import random
import requests

def main(instance_id):
    try:
        ec2_client = boto3.client('ec2')
        detach_iam_role(ec2_client, instance_id)
        isolate_with_sg(ec2_client, instance_id)
    except Exception as e:
        print(str(e))

def detach_iam_role(ec2_client, instance_id):
    response = ec2_client.describe_iam_instance_profile_associations(
        Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                    instance_id,
                ]
            },
        ]
    )

    for association in response['IamInstanceProfileAssociations']:
        response = ec2_client.disassociate_iam_instance_profile(
            AssociationId=association['AssociationId']
        )
    
    print("Deassociated IAM role for instance " + instance_id)
    print(str(response))

def isolate_with_sg(ec2_client, instance_id):
    id = random.randint(10000000, 99999999)

    # describe the instance to get its VPC ID
    response = ec2_client.describe_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    vpc_id = response['Reservations'][0]['Instances'][0]['VpcId']

    # create a new security group
    response = ec2_client.create_security_group(
        Description='SG to isolate VMs by SOC team',
        GroupName='soc_isolate_' + str(id),
        VpcId=vpc_id
    )
    security_group_id = response['GroupId']

    print("Created Security Group " + security_group_id)

    # Get my IP
    # send a GET request to the public IP address API
    response = requests.get('https://api.ipify.org')
    public_ip = response.text

    # Block all inbound traffic
    ec2_client.revoke_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': '-1',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0'
                    }
                ]
            }
        ]
    )

    # Block all inbound traffic except for my IP
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [
                {
                    'CidrIp': public_ip + '/32'
                }
            ]
        }
        ]
    )

    # Block all outbound traffic
    ec2_client.revoke_security_group_egress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': '-1',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0'
                    }
                ]
            }
        ]
    )

    # Attach security group to instance
    ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[
            security_group_id
        ]
    )
    print("Associated Security Group to instance " + instance_id)


if __name__=="__main__":
    main("")