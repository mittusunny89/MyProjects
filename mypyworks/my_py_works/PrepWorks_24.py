#WAP to execute the command 'ls -a' in a remote Linux server directory and read the filename and size that has read , write and execute permissions for all users in that server. Write the filename and size into a local txt file.

import paramiko
import re
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost',port = 22,username = 'ageorge', password ="bayshore1234$")
stdin,stdout,stderr= ssh.exec_command("ls -l /home/mittoos")
items = stdout.read().decode()
sitems = items.splitlines()
#print(sitems)
myfiles =[]
for line in sitems:
    if "-rwxrwxrwx"in line:
        myfiles.append(line)
print(myfiles)
