#! /usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

def is_evenly_divis (lst, num):
  for i in lst:
    if num % i != 0:
      return False
        
  return True



num = 20
while True:
  if is_evenly_divis ( range (2,21), num):
    print num
    break
  num += 20
    
    