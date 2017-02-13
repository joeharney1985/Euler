
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

def findMaxDigits():
    n_digits = 1
    value = 10 ** n_digits -1
    nine_factorial = factorial(9)
    while (n_digits * nine_factorial > value):
        print "{} > {}".format(n_digits * nine_factorial, value)
        n_digits += 1
        value = 10 ** n_digits -1
    return n_digits

lookup_table = [factorial(i) for i in range(10)]

def isCuriousNumber(n):
    str_n = str(n)
    sum = 0
    for digit in str_n:
        sum += lookup_table[int(digit)]
        
    return sum == n
    
n_digits = findMaxDigits()
solutions = [i for i in range(3, 10**n_digits) if isCuriousNumber(i)]

print solutions

print sum(solutions)
    
