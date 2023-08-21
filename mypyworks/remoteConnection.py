'''
import paramika
import subprocess

ssh = paramika.SSHClient()

ssh.connnect('server_name', username = 'user',password ='pwd'))


import subprocess
command = "grep Online file.txt"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)

'''
#method overloading

def add(*args):
    result = 0
    for item in args:
        result += item
    print(result)

add(1)
add(1,2)