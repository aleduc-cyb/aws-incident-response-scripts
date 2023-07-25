# aws-incident-response-scripts
This script allows you to perform various remediation actions on AWS resources using the command line. It provides a set of options to perform different tasks, such as stopping EC2 instances, creating snapshots of EC2 instances, resetting IAM user passwords, disabling IAM user accesses, disabling Lambda functions, and setting RDS databases and S3 buckets as private.

## Requirements
- Python 3.x
- AWS CLI configured with appropriate credentials and permissions
  - The appropriate permissions are described in the `iam_policy.json` file

## Installation

1. Clone this repository to your local machine:

`git clone https://github.com/aleduc-cyb/aws-incident-response-scripts.git`

`cd aws-incident-response-scripts`


2. Install the required Python packages:

`pip install -r requirements.txt`


## Usage

Run the script from the command line with the desired options to perform the corresponding remediation action.

`python main.py [options]`

### Options

- `-es` or `--ec2_stop`: Stop an EC2 instance. Provide the instance ID with the `-i` or `--instance` flag.
- `-ep` or `--ec2_snap`: Create a snapshot of an EC2 instance. Provide the volume ID with the `-v` or `--volume` flag.
- `-ir` or `--iam_reset`: Reset a user's IAM password and output the new password. Provide the username with the `-u` or `--username` flag.
- `-id` or `--iam_dis`: Disable keys and console access for a user. Provide the username with the `-u` or `--username` flag.
- `-ld` or `--lmbd_dis`: Disable a Lambda function. Provide the function name with the `-f` or `--function` flag.
- `-rp` or `--rds_priv`: Set an RDS database as private. Provide the database name with the `-d` or `--database` flag.
- `-sp` or `--s3_priv`: Set an S3 bucket as private. Provide the bucket name with the `-b` or `--bucket` flag.
- `-ei` or `--ec2_isol`: Isolate a VM by creating a security group. Provide the instance ID with the `-i` or `--instance` flag.

## Examples

- Stop an EC2 instance:

`python main.py -es -i <instance_id>`

- Create a snapshot of an EC2 instance:

`python main.py -ep -v <volume_id>`

- Reset a user's IAM password:

`python main.py -ir -u <username>`

- Disable keys and console access for a user:

`python main.py -id -u <username>`

- Disable a Lambda function:

`python main.py -ld -f <function_name>`

- Set an RDS database as private:

`python main.py -rp -d <database_name>`

- Set an S3 bucket as private:

`python main.py -sp -b <bucket_name>`

- Isolate a VM by creating a security group:

`python main.py -ei -i <instance_id>`

## Important Note

Please use this script responsibly and ensure that you have appropriate permissions to perform the remediation actions on AWS resources.

## Disclaimer

The authors of this script are not responsible for any damages or misuse of the script. Use it at your own risk.

If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Happy remediation!
