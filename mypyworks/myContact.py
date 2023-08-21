#add/edit contact in contact book
import json
class MyContactBook(object):
    def __init__(self):
        try:
            with open("phone_directory.json","r") as f:
                self.phone_dir = json.load(f)
              
        except FileNotFoundError:
            self.phone_dir = []
        except Exception as e:
            print(type(e).__name__)    

          
    def user_menu(self):
        while True:       
            try:
                user_choice = int(input( "Enter your choice to start: \n 1. Add a contact \n 2. Show the contacts \n 3. Edit a contact \n 4. Exit \n "))    
           
            except:
                user_choice = int(input("Please enter a valid choice: "))
                continue
        
            if user_choice == 1:
                self.add_contact()
            elif user_choice == 2:
                self.show_contacts()
            elif user_choice == 3:
                self.edit_contact()
            elif user_choice == 4:
                break
            else:
                print("Please enter a valid choice: ")     
                

    def add_contact(self):
        name = input("Enter the name to add: ")
        phonenum = int(input(f"Enter the phone number of {name}: "))
        while len(str(phonenum)) != 10:
            phonenum = int(input("Enter a valid phone number: "))
        try: 
            contact = {"Name":name , "Phone Number": phonenum}
            print(contact)
            self.phone_dir.append(contact)
            print(self.phone_dir.append(contact))
            with open("phone_directory.json","w") as f:
                json.dump(self.phone_dir,f)
        except:
            print("error in add_contact")

    def show_contacts(self):
        try: 
            #with open("phone_directory.json","r") as f:
            #    self.phone_dir = json.load(f)
            print("Your directory has the below contacts:")
            for contact in self.phone_dir:
                print(f"{contact['Name']} : {contact['Phone Number']}")
        except:
            print("error in show contact")
        
    def edit_contact():
        try: 
            old_name = input("Select the contact to edit")
            new_name = input("Enter the new name: ")
            
                print(f"{contact['Name'] = new_name} ")
        except:
            print("error in show contact")
          

MyPhoneBook = MyContactBook()
MyPhoneBook.user_menu()