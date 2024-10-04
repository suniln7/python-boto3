# SSH and SFTP Python Scripts

## [Multi-Host SSH Connection with SFTP and Command Execution](./ssh-file-operations.py)

This Python script uses **Paramiko** to connect to multiple remote hosts via SSH with a private key and optional password authentication, transfer a file using SFTP, and execute commands on each host. Hosts are read from a file named `hosts`, and the script iterates over each host, performing the basic file operartions.



## [Single-Host SSH Connection with SFTP File Download](./python-ssh.py)

This Python script establishes an SSH connection to a single remote host and performs a file download using SFTP.
