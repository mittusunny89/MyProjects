#WAP to find the factorial of a number

def fact(n):
    fa_ct = n
    if n >1 :
        for i in range(n):
            fa_ct *=  (n-i) 
        print(f"The factorial is {fa_ct}")
    elif n == 0 or 1:
        print(f"The factorial is 1")
    else:
        print("Please enter a valid number")

n = int(input("Enter the number to find factorial "))
fact(n)
