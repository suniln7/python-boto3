import paramiko
import os

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

password = os.getenv("SSH_PASSWORD")

private_key_path = "./rancher.pem"

key = paramiko.RSAKey.from_private_key_file(private_key_path)

hostname = "192.168.39.160"
username = "rancher"

try:

    ssh.connect(hostname,username=username,pkey=key, password=password)

    ftp_client = ssh.open_sftp()
    ftp_client.get('./node-token.txt', './node-token.txt')

    stdin , stdout , stderr = ssh.exec_command('ls -la')

    output = stdout.read().decode()

    print(output)

    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")
finally:
    ftp_client.close()
    ssh.close()
