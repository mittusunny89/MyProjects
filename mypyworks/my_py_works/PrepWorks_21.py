#Write a Python program to read last n lines of a file
import re
def read_lines():
    with open("C:\git\MyProjects\mypyworks\my_py_works\Valayoosai.txt","r+") as mfile:
        note = mfile.readlines()
        print(note[:5])
        for line in note:
            notes= re.sub(r"\n","",line)
            
read_lines()