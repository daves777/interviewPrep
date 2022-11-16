# Problem:
# We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the
# total n + 1 numbers, find the missing number.

# Example:
# Input: [4, 0, 3, 1]
# Output: 2

# Solution:
# This problem follows the Cylic Sort pattern. Since the input array contains unique numbers from the range 0 to n, we can use a
# similar strategy as in Cyclic sort to place the numbers in their correct index. Once we have every number in its correct place,
# we can iterate the array to find the index which does not have the correct number, and that index will be our missing number.

# There are two differences with cylcic sort.
# 1. In this problem the numbers are ranged from 0 to n as opposed to 1 to n. That means the index that the number should be at
#    will be the same as the number itself. Since the array has n numbers, that means array indices will range from 0 to n - 1.
#    That also means we must ignore the number n since we can't place it in the array
# 2. Because of the above index situation, we will have an extra number that won't fit in the resulting array. Thus, whenever
#    we swap indices, we must first check and ensure that the number is within the valid range

# Time Complexity: O(N)
# In the while loop, although we are not incrementing the index i when swapping the numbers, this will result in more than n
# iterations of the loop. But in the worst-case scenario, the while loop will swap a total of n-1 numbers and once a number is at
# its correct index, we will move on to the next number by incrementing i. In the end, we iterate the input array again to find
# the first number missing from its index, so overall, our algorithm will take O(n) + O(n-1) + O(n) which is equivalent to O(n)

# Space Complexity: O(1)
# This algorithm runs in constant space O(1)

def find_missing_number(nums):
  current_index = 0
  while current_index < len(nums):
    correct_index = nums[current_index] # determine the index position the number should be at
    # if the number we're looking at is within the valid range and isn't at the correct index
    if nums[current_index] < len(nums) and nums[current_index] != nums[correct_index]:
      nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index] # swap the two numbers
    else:
      current_index += 1 # only iterate to next index if number we're looking at is in the correct index
  
  # iterate through the array again to find the first number missing from its index
  for i in range(len(nums)):
    if nums[i] != i:
      return i
      
  return len(nums)


def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()