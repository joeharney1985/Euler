"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def sumDigitsToPow(number, power):
    sum = 0
    for digit in str(number):
        sum += int(digit)**power
        #if sum > number:
         #   return 0
    return sum


def findMaxDigitsToTest(power):
    n_digits = 1
    max_val = (10**n_digits) - 1
    while max_val <= sumDigitsToPow(max_val, power):
        n_digits += 1
        max_val = (10**n_digits) - 1
    return n_digits


def getAllNumbersWhoseDigitsToThisPowerSumToTheNumber(power):
    max_digits_to_test = findMaxDigitsToTest(power)
    return [i for i in range(2, 10**max_digits_to_test) if i == sumDigitsToPow(i, power)]

all = getAllNumbersWhoseDigitsToThisPowerSumToTheNumber(5)

print all
print sum(all)

               
    
    


#for i in range(10):
#    max_number = 10**i -1
#    if max_number > sumDigitsToPow(max_number, 5):
#        print "breaking at {} digits".format(i)
#        break

#for i in range(100000):
#    print "{}, {}".format(i, sumDigitsToPow(i, 4))
