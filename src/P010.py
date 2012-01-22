#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from Prime import is_prime

# starting summation at 2 because thats the first prime
summation = 2

# starting i at 3 so we do not have to check all the even number to see if they
# are prime.
i = 3
while i < 2000000:
  if is_prime(i):
    summation += i
  i += 2
  
print summation