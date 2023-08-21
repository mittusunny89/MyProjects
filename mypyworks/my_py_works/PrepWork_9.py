#WAP to create a subclass of string and add extend method to add iterable elements
'''
class SubStr(str):
    def __init__(self,mystring):
        str().__init__()
        self.mystring = mystring
    def extend(self,itr):
        secstr = ''
        for elem in itr:
            secstr += str(elem)
        self.mystring += secstr

mystr = "abcd"
obj = SubStr(mystr)
obj.extend([1,2,3])
print(obj.mystring)
'''


class SubStr(str):
    def __init__(self):
       
        str().__init__()
        #self.mystring = mystring
    def extend(self,mystring,itr):
        
        secstr = ''
        for elem in itr:
            secstr += str(elem)
        mystring += secstr
        print(mystring)

mystr = "abcd"
obj = SubStr()
obj.extend(mystr,[1,2,3])
print(obj.extend)
