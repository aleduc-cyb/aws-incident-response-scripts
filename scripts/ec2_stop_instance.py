import boto3

def main(instance_id):
    try:
        ec2_client = boto3.client('ec2')

        response = ec2_client.stop_instances(
            InstanceIds=[instance_id]
        )

        print("Performed action to stop instance " + instance_id)
        print(str(response))

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()