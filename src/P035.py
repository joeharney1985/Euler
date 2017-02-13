"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from Prime import is_prime

n = 1000000
#n = 100



# rule out any prime which could contains an even number because its 
# has a permutation which is even.
kEvenDigits = ['0', '2', '4', '6', '8']
def primeDoesntContainEvenDigit(number_str):
    # if its prime and a single digit return (2 is still prime)
    if len(number_str) == 1: return True
    for even in kEvenDigits:
        if even in number_str: return False
    return True

all_potential_primes = set([str(i) for i in range(n) if primeDoesntContainEvenDigit(str(i)) and is_prime(i)])

#all_potential_primes = set([prime for prime in all_primes if primeDoesntContainEvenDigit(prime)])

#all_potential_primes = set(all_primes)

print len(all_potential_primes)


solutions = []

def setPeek(s):
    elem = s.pop()
    s.add(elem)
    return elem

def getRotations(str_val):
    l = len(str_val)
    return [str_val[i:l] + str_val[0:i] for i in range(l)]

while len(all_potential_primes) > 0:

    p = setPeek(all_potential_primes)
    perm_set = set(getRotations(p))
    all_found = True
    for permutation in perm_set:
        if permutation in all_potential_primes:
            all_potential_primes.remove(permutation)
        else:
            all_found = False
    if all_found:
        solutions.extend(perm_set)

print solutions

print len(solutions)
    


