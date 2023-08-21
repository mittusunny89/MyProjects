# Create a boolean array of size 10^6+1 and initialize all entries as True
sieve = [True] * (10**6 + 1)

# Mark all the multiples of 2, 3, 5, and so on as False
for i in range(2, int(10**6**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, 10**6 + 1, i):
            sieve[j] = False

# Print or store the numbers that remain True as prime numbers
primes = []
for i in range(2, 10**6 + 1):
    if sieve[i]:
        primes.append(i)
        # print(i)

# Print the number of prime numbers found
print(f"There are {len(primes)} prime numbers between 1 and 10^6.")
