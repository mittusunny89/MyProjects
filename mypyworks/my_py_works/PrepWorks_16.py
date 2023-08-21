#Write a Python program to read a given CSV file as a dictionary and convert it into a JSON file
import json

#create a class with emplst line passed in to the constructor
class Employee():
    def __init__(self,empdet):
        self.emp_det_lst = empdet.split(',')
        self.empid = self.emp_det_lst[0]
        self.fname = self.emp_det_lst[1]
        self.lname = self.emp_det_lst[2]
        self.email = self.emp_det_lst[3]
        self.phone = self.emp_det_lst[4]
        self.hiredate = self.emp_det_lst[5]
        self.jobid = self.emp_det_lst[6]
        self.salary = self.emp_det_lst[7]
        self.commission = self.emp_det_lst[8]
        self.managerid = self.emp_det_lst[9]
        self.depid = self.emp_det_lst[10]
    def set_empid(self,empid):
        self.empid = empid
    def set_fname(self,fname):
        self.fname = fname
    def set_lname(self,lname):
        self.lname = lname
    def set_email(self,email):
        self.email = email
    def set_phone(self,phone):
        self.phone = phone
    def set_hiredate(self,hiredate):
        self.hiredate = hiredate
    def set_jobid(self,jobid):
        self.jobid = jobid
    def set_salary(self,salary):
        self.salary = salary
    def set_commission(self,commission):
        self.commission = commission
    def set_managerid(self,managerid):
        self.managerid = managerid
    def set_depid(self,depid):
        self.depid = depid

    def get_empid(self):
        return self.empid
    def get_fname(self):
        return self.fname
    def get_lname(self):
        return self.lname
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    def get_hiredate(self):
        return self.hiredate
    def get_jobid(self):
        return self.jobid
    def get_salary(self):
        return self.salary
    def get_commission(self):
        return self.commission
    def get_managerid(self):
        return self.managerid
    def get_depid(self):
        return self.depid

#read csv file. Get a list of strings each contains a line of data
with open("C:\git\MyProjects\mypyworks\my_py_works\employees.csv ",'r+') as emp:
    emplst = emp.readlines()
headline = emplst[0]
emplst.pop(0)
empobjects = []
for line in emplst:
    empobjects.append(Employee(line))

jdict = {}
with open("C:\git\MyProjects\mypyworks\my_py_works\employees.json ",'w+') as jemp:
    for k in empobjects: 
        jdict[k.get_fname()] =  {
                "emp_id"     : k.get_empid(),
                "first_name" : k.get_fname(),
                "last_name"  : k.get_lname(),
                "email"      : k.get_email(),
                "phone"      : k.get_phone(),
                "DOJ"        : k.get_hiredate(),
                "Job_id"     : k.get_jobid(),
                "Salary"     : k.get_jobid(),
                "Commission" : k.get_commission(),
                "manager"    : k.get_managerid(),
                "dep_id"     : k.get_depid()
     
            }
        
        
    json.dump(jdict,jemp,indent=2)
        

    


