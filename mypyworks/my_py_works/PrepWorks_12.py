#question: Write a Python program to read first n lines of a file from a local folder location.

def read_file(file,n):
    with open(file,'r+') as f:
        for i in range(n):
            lines = f.readline()
            print(lines)
def read_slice_file(file,n):
    with open(file,'r+') as f:
        lines = f.readlines(90)
        print(lines)

#read_file("C:\git\MyProjects\mypyworks\my_py_works\Valayoosai.txt",5)
#read_slice_file("C:\git\MyProjects\mypyworks\my_py_works\Valayoosai.txt",5)



#read all lines from the following IIS log file that occurred  between the time 15:00:00 and 19:00:00

#read all lines
def read_log(filename): 
    with open(filename, 'r+') as f:
        content = f.readlines() #The readlines() method returns a list containing each line in the file as a list item.
        #extract the line conatining POST or GET text to a new file
        relevant = []
        for line in content:
            if 'GET' or 'POST' in line:
                relevant.append(line)
        #read the lines in new file. it will be a list of strings
        #split each string into list and get the index position of time field and extract required value 
        req_logs = []
        for line in relevant:
            loglst = line.split()
            if '15:00:00' < loglst[1] < '19:00:00':
                req_logs.append(line)
        return req_logs
      
def write_req_logs(file,req_logs):
    with open(file,'w+') as lf:
        lf.writelines(req_logs)
        lf.seek(0)
        y = lf.read()
        print(y)
        
x = read_log('C:\git\MyProjects\mypyworks\my_py_works\iislog.log')
#print(x)
write_req_logs(r'C:\git\MyProjects\mypyworks\my_py_works\rel_logs.txt', x)
