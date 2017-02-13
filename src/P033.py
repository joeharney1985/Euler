"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def reducesCuriously(canceling_digit, numerator, denominator):
    # get rid of the trival examples
    if canceling_digit == '0': return False
    reduced_n = float(numerator[(numerator.find(canceling_digit)+1) % 2])
    reduced_d = float(denominator[(denominator.find(canceling_digit) +1) % 2])
    if reduced_n == 0 or reduced_d == 0:
        return False
    return  int(numerator) / reduced_n == int(denominator) / reduced_d
    
def isCuriousFraction(numerator, denominator):
    numerator_str = str(numerator)
    denominator_str =  str(denominator)
    for digit in numerator_str:
        if digit in denominator_str:
            if reducesCuriously(digit, numerator_str, denominator_str):
                return True
    return False
    

    
answers = []

for denominator in range(10,100):
    for numerator in range (10,denominator):
        if isCuriousFraction(numerator, denominator):
            answers.append([numerator, denominator])

print answers


prod_n = 1
prod_d = 1
for fraction in answers:
    prod_n *= fraction[0]
    prod_d *= fraction[1]

print "{}/{}".format(prod_n, prod_d)

print prod_n / float(prod_d)
