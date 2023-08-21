#write a program to check if a given number is prime by accepting input

def check_prime(num):
    counter =0
    if num <=1:
        print("It is not a prime number")
    else:
        for i in range(2,num//2):
            if num%i == 0 :
                
                print("It is NOT a prime number")
        else:
            print("It is a prime number")
num = input("Enter the number to check as prime or not ")
check_prime(int(num))