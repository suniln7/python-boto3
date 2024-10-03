import boto3
import string
import random

def generate_random_string(length=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


ec2 = boto3.client('ec2')

securitygroup_name = "alltraffic"

response = ec2.run_instances(
    InstanceType="t2.micro",
    MaxCount=3,
    MinCount=3,
    ImageId="ami-0ebfd941bbafe70c6",
    KeyName='python-ec2',
    SecurityGroups=[securitygroup_name]
    
)

output_file = "created_instances.txt"

with open(output_file,'a') as f:
    for instance in response['Instances']:
        instance_id = instance['InstanceId']
        private_ip = instance.get('PrivateIpAddress', 'N/A')
        random_suffix = generate_random_string()

        ec2.create_tags(
            Resources = [instance_id],
            Tags = [
                {
                    'Key': 'Name',
                    'Value': f'test-{random_suffix}'
                }
            ]
        )

        f.write(f"{instance_id} {private_ip}\n")

print(response)

with open(output_file, 'r') as f:
    file_content = f.read()

print("\nContents of created_instance.txt:")
print(file_content)
