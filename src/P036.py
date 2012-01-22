"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


"""


        
def toBin (dec):
  if dec == 0:
    return ""
  return toBin(dec>>1) + str(dec%2)

def is_pal (in_str):
  length = len(in_str)
  if length < 2:
    return True
  return in_str[0] == in_str[length-1] and is_pal(in_str[1:length-1])
  
summation = 0
for i in range(1,1000000,2):
  if is_pal(str(i)) and is_pal(toBin(i)):
    summation += i
    
print summation

  