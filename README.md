# EC2 Management Scripts

This repository contains Python scripts that utilize Boto3 to manage Amazon EC2 instances. Each script serves a specific purpose, as outlined below.

## [create-ec2.py](./create-ec2.py)

This script utilizes Boto3 to launch a single Amazon EC2 instance of type `t2.micro` using the specified AMI (`ami-0ebfd941bbafe70c6`) and key pair (`thethings`). After execution, it prints the response from AWS, detailing the newly created instance.

## [delete_ec2.py](./delete_ec2.py)

This script uses Boto3 to terminate an Amazon EC2 instance with the specified instance ID (`i-0afa7288db6955999`). Upon execution, it prints the response from AWS, confirming the termination of the instance.

## [keypair.py](./keypair.py)

This script uses Boto3 to create a new Amazon EC2 key pair named `python-ec2`. It saves the private key to a file (`python-ec2.pem`) with secure permissions (400). After execution, it prints the response from AWS, which includes details about the created key pair.

## [create_ec2_2.py](./create_ec2_2.py)

This Python script utilizes the Boto3 library to launch three Amazon EC2 instances of type `t2.micro` using the specified AMI (`ami-0ebfd941bbafe70c6`). Each instance is associated with a key pair named `python-ec2` and a security group named `alltraffic`. To ensure unique identification, the script dynamically tags each instance with a name formatted as `test-<random_suffix>`, where `<random_suffix>` is a randomly generated four-letter string. The instance IDs and their corresponding private IP addresses are recorded in a file named `created_instances.txt`. After the instances are created, the script prints the response from AWS detailing the created instances and displays the contents of the output file. To use this script, ensure that Boto3 is installed and your AWS credentials are configured. Note that the specified AMI ID and security group must exist in your AWS account and region.

## [delete_ec2_2.py](./delete_ec2_2.py)

This Python script uses the Boto3 library to terminate Amazon EC2 instances whose IDs are listed in the `created_instances.txt` file. It reads the file, extracts the instance IDs, and stores them in a list. If the list of instance IDs is not empty, the script sends a termination request to AWS for those instances and prints a confirmation message along with the termination response. If no instance IDs are found in the file, it notifies the user accordingly.

## [python-ssh-file-operations](./python-ssh-file-operation/)

Python scripts uses **Paramiko** to establish SSH connections, transfer files via SFTP, and execute remote commands. It supports both single and multi-host operations: . SSH authentication is done via a private key and optional password, fetched securely from environment variables. Proper error handling and resource management ensure secure execution and cleanup of connections.