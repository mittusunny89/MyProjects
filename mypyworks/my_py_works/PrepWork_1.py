#write a program to swap two numbers by takinginput from user

def swap_num(num1,num2):
    tmp = num1
    num1= num2
    num2 =tmp
    print(f"The first number is {num1} and second number is {num2}")

num1 =input("Enter the first number ")
num2 =input("Enter the second number ")
swap_num(num1,num2)