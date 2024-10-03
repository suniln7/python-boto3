import boto3
import os


ec2 = boto3.client('ec2')
keypair_name = "python-ec2"
keypair_response = ec2.create_key_pair(KeyName=keypair_name)

# Save the private key to a file
private_key = keypair_response['KeyMaterial']
private_key_file = f"{keypair_name}.pem"

with open(private_key_file, 'w') as f:
    f.write(private_key)

os.chmod(private_key_file, 0o400)

print(keypair_response)