#! /usr/bin/python

#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

number = 600851475143

def prime_factorize (num, primes):
  i = 2
  while i < num + 1: 
    if True:#is_prime (i):
      if num / float(i) == 1:
        primes.append(i)
        return primes
      if num % i == 0:
        primes.append(i)
        return prime_factorize(num / i, primes)
      i += 1
        
        
factors = []
prime_factorize (number, factors )

prod = 1;
for i in factors:
  prod *= i

assert prod == number

print factors.pop()

    