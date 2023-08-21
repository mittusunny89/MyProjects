

class Jets:

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country
        
        


class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country
        
        
        
#Type your code here

class AJS37(Jets):
    def __init__(self):
        Jets.__init__(self,'AJS37', 'Sweden')
        
b = AJS37()   

print(b.name) 
print(b.origin)

