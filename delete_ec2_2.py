import boto3
instances_file = "created_instances.txt"
instances = []
with open(instances_file,'r') as f:
    
    for line in f :
        instance_id = line.split()[0]
        instances.append(instance_id)

# print(instaces) 

ec2 = boto3.client('ec2')

if instances:
    response = ec2.terminate_instances(InstanceIds=instances)
    print("Terminating the following instances:", instances)
    print("Termination response:", response)
else:
    print("No instance IDs found to terminate.")