#! /usr/bin/python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def naive():
  total = 0
  for i in range(1000):
    if i % 3 == 0:
      total += i
    elif i % 5 == 0:
      total += i
  return total

def comprehension():
  return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

def smart_increment(): 
  total = 0
  for i in range(0, 1000, 3):
    total += i
  for i in range(0, 1000,5):
    total += i

  # remove duplicates
  for i in range(0, 1000, 3 * 5):
    total -= i
  return total


print naive()


print comprehension() 

print smart_increment()
