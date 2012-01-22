

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10,001st prime number?

from Prime import is_prime

i = 1
n = 0
while n < 10001:
  i += 1
  if is_prime (i):
    n += 1
  
print i


  