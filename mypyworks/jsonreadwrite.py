#add/edit contact in contact book
import json
class MyContactBook():
    def UserMenu(self):
        UserChoice = int(input( "Enter your choice to start: \n 1. Add a contact \n 2. Show the contacts \n 3. Edit a contact \n"))    
        
        if UserChoice == 1:
            pass
        elif UserChoice == 2:
            print("I will show you the saved contatcs")
            self.ShowContacts(self.PhoneDir)
        elif UserChoice == 3:
            pass
    def WriteToFile(self,name,phonenum):

        PhoneDir = {"Name":name , "Phone Number": phonenum}
        with open("PhoneDirectory.json","wt+") as f:
            json.dump( PhoneDir, f)

        with open("PhoneDirectory.json","r") as f:
            mydirectory =  json.load(f)
            print(mydirectory)
        return(PhoneDir)

    def ShowContacts(self,PhoneDir):
        print("Your directory has the below contacts \n{} ':' {}" .format(name,phonenum))

MyPhoneBook = MyContactBook()
MyPhoneBook.UserMenu()