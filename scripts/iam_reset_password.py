import boto3
import random
import string

def main(username):
    try:
        iam_client = boto3.client('iam')

        # Generate random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(16))

        response = iam_client.update_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
        )

        print('Performed action to change password for ' + username)
        print('New password :' + password)
        print(str(response))

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()