#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math 

def find_tripple():
  for a in range (1, 1001):
    for b in range (1, 1001):
      c = math.sqrt(a * a + b * b)
      summation = a + b + c
      if summation == 1000:
        print a * b * c
        return
      
find_tripple() 
      
  