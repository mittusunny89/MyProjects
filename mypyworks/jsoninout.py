import json
class MyContactBook():
    def UserMenu(self):
        UserChoice = int(input( "Enter your choice to start: \n 1. Add a contact \n 2. Show the contacts \n 3. Edit a contact \n"))    

        if UserChoice == 1:
            name = input("Enter the name to add: ")
            phonenum = int(input(("Enter the phone number of " + name + ': ')))
            while len(str(phonenum)) != 10:
                phonenum = int(input("Enter a valid phone number: "))
                                      
            self.WriteToFile(name, phonenum)

        else :
            print("I will show you the saved contatcs")
            self.ShowContacts(WriteToFile,name,phonenum)
    def WriteToFile(self,name,phonenum):

        PhoneDir = {"Name":name , "Phone Number": phonenum}
        with open("PhoneDirectory.json","wt+") as f:
            json.dump(  PhoneDir, f)

        with open("PhoneDirectory.json","r") as f:
            mydirectory =  json.load(f)
            print(mydirectory)
        return(PhoneDir)

    def ShowContacts(self,WriteToFile,name,phonenum):
        print("Your directory has the below contacts \n{} ':' {}" .format(name,phonenum))
        return WriteToFile(name,phonenum)
    
MyPhoneBook = MyContactBook()
MyPhoneBook.UserMenu()