import boto3

def main(function_name):
    try:
        lambda_client = boto3.client('lambda')
        
        response = lambda_client.put_function_concurrency(
            FunctionName=function_name,
            ReservedConcurrentExecutions=0
        )
        
        print("Performed call to stop Lambda function " + function_name)
        print(str(response))

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()