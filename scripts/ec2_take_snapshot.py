import boto3

def main(volume_id):
    try:
        ec2_client = boto3.client('ec2')

        response = ec2_client.create_snapshot(
            Description='Snapshot from SOC for investigation',
            VolumeId=volume_id
        )

        print("Performed action to snapshot volume " + volume_id)
        print(str(response))

    except Exception as e:
        print(str(e))
    
if __name__=="__main__":
    main()