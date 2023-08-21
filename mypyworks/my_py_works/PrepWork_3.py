#Write a program to print fibanocci series

fib = [0,1]

def write_fib(X):
    m = fib[0]
    n = fib[1]
    for i in range(2,X):
        #fib[i] = m+n
        fib.append(m+n)
        m = fib[i-1]
        n = fib[i]
    print(fib)

write_fib(5)       
