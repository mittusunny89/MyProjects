#Write a Python program that creates a generator function that generates all prime numbers between two given numbers

'''
prime number - have only two factors 1 and n
divide the n by 1 to n

'''
def is_prime(n):
    if n==2:
        return True
    elif n>2:
        counter = 0
        for i in range(1,n+1):
            if n%i == 0:
                counter +=1
        if counter ==2:
            return True
    else:
        return False



def prime_gene(start,stop):
    for i in range(start,stop+1):
        if is_prime(i):
            yield i

start = int(input("Enter the starting number: "))
stop = int(input("Enter the stop number: "))

prime_gen = prime_gene(start,stop)
primes =[]
for num in prime_gen:
    primes.append(num)

print(primes)
