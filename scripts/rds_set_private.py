import boto3

def main(db_name):
    try:
        rds_client = boto3.client('rds')

        response = rds_client.modify_db_instance(
            DBInstanceIdentifier=db_name,
            PubliclyAccessible=False,
            ApplyImmediately=True
        )

        print("Performed call to set " + rds_client + " as private")
        print(str(response))

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()