import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
    InstanceIds=[
        'i-0afa7288db6955999'
    ]
)

print(response)