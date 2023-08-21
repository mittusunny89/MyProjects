#Write a Python program to create a class representing a shopping cart. 
#Include methods for adding and removing items, and calculating the total price.

import json
#shopping cart
class ShoppingCart():
    def __init__(self,cart):
        self.cart = cart
       # self.pricedict = pricedict
#add items
    def add_cart(self):
        print(f"Select the items to your cart:")
        with open("C:\git\MyProjects\mypyworks\my_py_works\items.json") as menufile:
            menu = json.load(menufile)
        for key in menu.keys():
            print(f"{key} \n Name: {menu[key]['name']} \n price: {menu[key]['price']}")
            
        '''for key, value in self.pricedict.items (): # This will loop over the key-value pairs of the dictionary
            print (f"{key} : {value}")'''
      
        item =input().split(',')
        for elem in item:
            self.cart.append(elem)
        print(self.cart)
        self.modify_cart(self.cart)
        return self.cart
  

#modify cart
    def modify_cart(self,cart):
        opt = input("Do you want to remove any item from your cart? yes/no \n")
        if opt == 'yes':
            item = input("Selet the items to be removed: ")
            self.cart.remove(item)
        input("Press 'Enter' to calculate price: ")
        print(self.cart)
        return self.cart
#calculate price
    def calc_price(self,mycart):
        sum = 0
       
        with open("C:\git\MyProjects\mypyworks\my_py_works\items.json") as menufile:
            menu = json.load(menufile)
        for item in mycart:
            sum += menu[item]['price']
        print(f"The total amount is: {sum}")

cart = []
#pricedict = {"onion": 3, "chilli" : 2, "fish" : 20, "beef" : 25, "garlic": 4, "sugar": 4}

customer = ShoppingCart(cart)
mycart =customer.add_cart() 

customer.calc_price(mycart)
