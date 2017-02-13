"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.


The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is9PandigitalStr(number_str):
  if (len(number_str)) != 9:
    return False
  seen = [False] * 10
  seen[0] = True # we dont want zero in our number
  for i in range(9):
    digit = int(number_str[i])
    if seen[digit]: return False
    seen[digit] = True
  return True

def is9Pandigital(multiplicand, multiplier, product):
  return is9PandigitalStr(str(multiplicand) + str(multiplier) + str(product))

pandigital_products = set()

for multiplicand in range(2, 9876):
  for multiplier in range(2, 9876):
    product = multiplicand * multiplier
    if is9Pandigital(multiplicand, multiplier, product):
      pandigital_products.add(product)
      
print pandigital_products

print 

print sum(pandigital_products)

