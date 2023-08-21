#Write a Python program to sort a given dictionary by key
import json
class SortDict():
    def __init__(self):
        #self.mydict = mydict
        pass
    
    def sort_dict(self):
        with open ("C:\git\MyProjects\mypyworks\my_py_works\employees.json",'r+') as f:
            mydict = json.load(f)
            skey = []
            for item in mydict.keys():
                skey.append(item)
        
            sdict = {}
            for k in sorted(skey):
                val = mydict[k]
                sdict[k] = val 
                print(sdict)
            with open ("C:\git\MyProjects\mypyworks\my_py_works\employees.json",'w+') as f:
                json.dump(sdict,f, indent=4)
           
sort = SortDict()
sort.sort_dict()
