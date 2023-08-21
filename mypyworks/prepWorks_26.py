def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n//2):
    if n % i == 0:
      return False
  return True

def largest_prime_in_range(a, b):
  for i in range(b, a - 1, -1):
    if is_prime(i):
      return i

print(largest_prime_in_range(2, 1000000)) # prints 97
