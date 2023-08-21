# Import the logging module
import logging

# Configure the logging level and format
logging.basicConfig(filename = 'my_prime_error2.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Create a logger object with the name 'prime'
logger = logging.getLogger('prime')

# Configure the logger level and format
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
# Define a function to check if a number is prime
def is_prime(n):
    # If n is less than 2, it is not prime
    if n < 2:
        return False
    # Loop from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by i, it is not prime
        if n % i == 0:
            return False
    logging.warning(f"found  as prime")
    # If none of the above conditions are met, n is prime
    return True

# Define a function to find prime numbers within a range
def find_primes(start, end):
    # Create an empty list to store the prime numbers
    primes = []
    # Loop from start to end
    for n in range(start, end + 1):
        # Check if n is prime using the is_prime function
        if is_prime(n):
            # If n is prime, append it to the primes list
            primes.append(n)
            # Log an info message with the prime number found
            logging.info(f'Found a prime number: {n}')
    # Return the primes list
    return primes

# Ask the user for the start and end of the range
start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))

# Call the find_primes function with the user input and print the result
result = find_primes(start, end)
print(f'The prime numbers between {start} and {end} are: {result}')
