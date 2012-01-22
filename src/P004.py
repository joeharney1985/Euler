#! /usr/bin/python


# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome (num):
  num_lst = list (str(num)) 
  rnum_lst = list(str(num))
  rnum_lst.reverse()
  return num_lst == rnum_lst

all_palindromes = set()

for i in range (100, 1000):
  for j in range (100, 1000):
    if is_palindrome(i * j):
      all_palindromes.add(i * j)
            

lst_all_p = list(all_palindromes)

lst_all_p.sort()

print lst_all_p.pop()