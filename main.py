import argparse
import scripts.ec2_stop_instance as ec2stop
import scripts.ec2_take_snapshot as ec2snap
import scripts.iam_reset_password as iamreset
import scripts.iam_revoke_accesses as iamdis
import scripts.lambda_disable_function as lmbddis
import scripts.rds_set_private as rdspriv
import scripts.s3_set_private as s3priv

def parse_args():
    # Parse the input arguments
    parser = argparse.ArgumentParser(description='Perform remediation actions on AWS')

    # All actions
    parser.add_argument('-es', '--ec2_stop', action='store_true', help='Stop an EC2 instance')
    parser.add_argument('-ep', '--ec2_snap', action='store_true', help='Create a snapshot of an EC2 instance')
    parser.add_argument('-ir', '--iam_reset', action='store_true', help='Reset a user password (outputs a password)')
    parser.add_argument('-id', '--iam_dis', action='store_true', help='Disable keys and console access for a user')
    parser.add_argument('-ld', '--lmbd_dis', action='store_true', help='Disables a Lambda function')
    #parser.add_argument('-rp', '--rds_priv', action='store_true', help='Sets a RDS database as private')
    parser.add_argument('-sp', '--s3_priv', action='store_true', help='Sets a S3 as private')

    # All potential IDs to pass
    parser.add_argument('-u', '--username', type=str, help='Name of the user to investigate')
    parser.add_argument('-i', '--instance', type=str, help='ID of the EC2 instance to stop')
    parser.add_argument('-v', '--volume', type=str, help='ID of the volume to backup')
    parser.add_argument('-f', '--function', type=str, help='Name of the function to disable')
    #parser.add_argument('-d', '--database', type=str, help='Name of the database to set as private')
    parser.add_argument('-b', '--bucket', type=str, help='Name of the bucket to set as private')

    return parser.parse_args()

def main():
    # Parse input arguments
    args = parse_args()

    # Check whether flags are ok
    input_checks(args)

    # Run actions according to user input
    run_actions(args)


def input_checks(args):
    if args.ec2_stop and not (args.instance):
        print("Please specify an instance")
        exit()

    if args.ec2_snap and not (args.volume):
        print("Please specify a volume")
        exit()

    if args.iam_reset and not (args.username):
        print("Please specify a username")
        exit()

    if args.iam_dis and not (args.username):
        print("Please specify a username")
        exit()

    if args.lmbd_dis and not (args.function):
        print("Please specify a function name")
        exit()

    if args.rds_priv and not (args.database):
        print("Please specify a database name")
        exit()

    if args.s3_priv and not (args.bucket):
        print("Please specify a bucket name")
        exit()

def run_actions(args):
    if args.ec2_stop:
        ec2stop.main(args.instance)

    if args.ec2_snap:
        ec2snap.main(args.volume)

    if args.iam_reset:
        iamreset.main(args.username)

    if args.iam_dis:
        iamdis.main(args.username)

    if args.lmbd_dis:
        lmbddis.main(args.function)

    if args.rds_priv:
        rdspriv.main(args.database)

    if args.s3_priv:
        s3priv.main(args.bucket)

if __name__=="__main__":
    main()