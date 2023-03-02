import boto3

def main(username):
    try:
        iam_client = boto3.client('iam')

        response = iam_client.list_access_keys(
            UserName=username
        )

        if 'AccessKeyMetadata' in response:
            for accesskey in response['AccessKeyMetadata']:
                accesskeyid = accesskey['AccessKeyId']
                response = iam_client.update_access_key(
                    AccessKeyId=accesskeyid,
                    Status='Inactive',
                    UserName=username
                )
                print("Performed action to deactivate access key " + accesskeyid + " for " + username)
                print(str(response))

        response = iam_client.delete_login_profile(
            UserName=username
        )

        print("Performed action to deactivate console login for " + username)
        print(str(response))

    except Exception as e:
        print(str(e))    

if __name__=="__main__":
    main()