import boto3


def main():
    session = boto3.Session()
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)


if __name__ == '__main__':
    main()
