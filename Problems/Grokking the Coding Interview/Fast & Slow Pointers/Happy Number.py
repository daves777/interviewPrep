# Problem:
# A number is a happy number if after repeatedly replacing it with a number equal to the sum of the square of all of
# its digits, leads to the number 1. Write a function that returns whether a number is a happy number or not.

# Solution:
# The process of finding if a number is a hppy number always ends in a cycle. It will either be in a cycle with a 
# set of numbers, or stuck on 1. We can use fast and slow pointers to find the cycle and see if it is tuck on the
# number 1 or not to determine if the number is happy

# Time Complexity: O(logN)
# The time complexity is dependent on the input number.

# Space Complexity: O(1)
# The algorithm runs in constant space

def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow) # move one step
    fast = find_square_sum(find_square_sum(fast)) # move two steps
    if slow == fast: # found cycle
      break
  return slow == 1 # see if cycle is stuck on '1'

def find_square_sum(num):
  sum = 0
  while num > 0:
    digit = num % 10 # extract the digit by using modulus operator to find remainder
    sum += digit * digit # add to sum
    num //= 10 # remove the digit in ones place
  return sum

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()