#find prime number between 2 and 1000

counter = 0
prime_num = [2]
for i in range(3, 10**6 ):
    
    flag = False
    for j in range(2,i):
        if(i%j == 0):
            flag = True
            break
    if(flag == False):
        prime_num.append(i)
        counter +=1

print(f"There are {counter} prime numbers and they are: \n {prime_num} ")