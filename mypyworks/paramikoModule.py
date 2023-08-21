import paramiko

# Create object of SSHClient and
# connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('localhost', port=22, username='ageorge',
			password='bayshore1234$', timeout=3)

# Execute command on SSH terminal
# using exec_command. use exec() when you need to dynamically run code that comes as a string.
#stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
stdin = 'ls -l /home/mittos'
stdin, stdout, stderr = ssh.exec_command(stdin)

#if len(stderr.read()) != 0:
print(f'There is an error as {stderr.read()}')

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