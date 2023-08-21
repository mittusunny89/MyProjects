#WAP to print region, manufacturer and year of a vehicles into a text file when its  VIN number given as input

import json
def read_vin():
    vin = input("Enter the VIN you have to check: ")
    with open(rf"C:\git\MyProjects\mypyworks\my_py_works\vin.json", 'r+') as f:
        dic = json.load(f)
        country = vin[0]
        manu = vin[1]
        model = vin[9]
        print(f"The country is : {dic['1'][country]}")
        print(f"The manufacturer is : {dic['2'][manu]}")
        print(f"The maodel is : {dic['10'][model]}")

read_vin()