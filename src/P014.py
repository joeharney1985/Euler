# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def is_odd(x):
  return x % 2 != 0

def find_seq_len (x):
  count = 1
  while x != 1:
    if is_odd(x):
      x = 3 * x + 1
    else :
      x = x/2
    count += 1
  return count

#print find_seq_len(13)
      
max_len = 0
max_seed = 1
for i in range (2, 1000001):
  cur_len = find_seq_len(i)
  if cur_len > max_len:
    max_len = cur_len
    max_seed = i
  
print max_len, max_seed