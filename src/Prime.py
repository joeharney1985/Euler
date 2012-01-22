# determines if the input x is prime 
import math

def is_prime (x):
  if x < 2:
    return False
  root = int(math.floor(math.sqrt(x)))
  for i in range (2, root+1):
    if x % i == 0:
      return False
  return True
