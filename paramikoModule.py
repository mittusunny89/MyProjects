#Program to extract files with size from a linux directory

import paramiko

# Create object of SSHClient and
# connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
#This policy allows the client to automatically add the host key of a server to the in-memory store of known host keys, without asking for confirmation from the user.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('localhost', port=22, username='ageorge',
			password='bayshore1234$', timeout=3)

# Execute command on SSH terminal
# using exec_command
#stdin, stdout, stderr = ssh.exec_command('show ip interface brief')

stdin, stdout, stderr = ssh.exec_command('ls -l /home/mittoos')

def find_files(mystring):
	mystring = stdout.read().decode()
	myitems = mystring.splitlines()
	myfiles = []
	for item in myitems:
		if '-rw-r--r--' in item:
			myfiles.append(item)
	for file in myfiles:	
		words = file.split()
	#print(words)	
		print(f'The file name is {words[-1]} with  size  {words[4]}')
find_files(stdout)
ssh.close()
