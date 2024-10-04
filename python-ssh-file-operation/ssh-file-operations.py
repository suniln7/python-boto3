import paramiko
import os
import gc  # Garbage collector

# Fetch password from environment variable
password = os.getenv("SSH_PASSWORD")

# Private key path
private_key_path = "./private.pem"

# Load private key
key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Username for SSH connection
username = "python-user"

# Open the hosts file and read lines
with open('hosts', 'r') as f:
    hosts = [line.strip() for line in f.readlines()]

# Iterate over each host
for host in hosts:
    try:
        print(f"Connecting to {host}...")

        # Use context manager to open SSH connection
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=username, pkey=key, password=password)

            # Use context manager to open SFTP session
            with ssh.open_sftp() as ftp_client:
                # Transfer file
                ftp_client.put('./node-token.txt', './py-file.txt')  # Adjust destination path as necessary
                print(f"File transferred to {host}")
                # ftp_client.remove('./py-file.txt')

                # Execute a command on the remote host
                stdin, stdout, stderr = ssh.exec_command('ls -la')
                
                # Capture the output
                output = stdout.read().decode()
                print(f"Listing on host {host}:\n{output}")
                print("--" * 40 + '\n')
                
                # Check for any errors
                error = stderr.read().decode()
                if error:
                    print(f"Error on {host}: {error}")

            # Explicitly close SFTP client
            ftp_client.close()

    except paramiko.SSHException as e:
        print(f"SSH connection error for {host}: {str(e)}")
    except Exception as e:
        print(f"An error occurred on {host}: {str(e)}")
        # Explicitly close SFTP client
        ftp_client.close()
    finally:
        # Explicitly close SSH connection
        ssh.close()

    # Force garbage collection after each host to avoid delayed cleanup issues
    gc.collect()

