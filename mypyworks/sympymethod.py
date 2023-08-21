# Import the sympy module
import sympy

# Use the primerange function to get an iterator of prime numbers between 1 and 10^6
primes = sympy.primerange(1, 10**6)

# Print or store the prime numbers
for p in primes:
    # print(p)
    pass

# Print the number of prime numbers found
print(f"There are {sympy.primepi(10**6)} prime numbers between 1 and 10^6.")
