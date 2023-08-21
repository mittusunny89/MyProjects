teststr = input("Enter the string to check as palindome or not: ")
print(type(teststr))
tmp = teststr[::-1]

if tmp == teststr:
    print("Its a palindrome")
else:
    print("not a aplindrome")