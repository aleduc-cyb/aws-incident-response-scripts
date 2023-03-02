import boto3

def main(bucket_name):
    try:
        s3_client = boto3.client('s3')   

        response = s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': False
            }
        )

        print("Performed call to set bucket " + bucket_name + " as private")
        print(str(response))

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()