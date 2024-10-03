import boto3



ec2 = boto3.client('ec2')

response = ec2.run_instances(InstanceType="t2.micro",
                         MaxCount=1,
                         MinCount=1,
                         ImageId="ami-0ebfd941bbafe70c6",
                         KeyName='thethings')
print(response)