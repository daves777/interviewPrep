# Problem:
# Given an unsorted array containing numbers, find the smallest missing positive number in it. Note that positive numbers
# start from 1.

# Example:
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'

# Solution:
# This problem follows the Cylic Sort pattern and is similar to find the missing number. The key difference here is that the
# numbers are not bound by any range, so we can have any number in the input array. We can place each number at the correct
# index, and ignore all numbers out of the range of the array. This includes negative numbers, and numbers greater than the
# length of the array. Then, we will iterate through the array and the first index with the wrong number will be the smallest
# missing positive number.

# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# We sort the array in place so we use constant space but it modifies the input array.

def find_first_smallest_missing_positive(nums):
  currentIndex = 0
  while currentIndex < len(nums):
    correctIndex = nums[currentIndex] - 1 # determine index position the number should be at
    # if number is valid (positive number less than length of array) and number at current index is not correct
    if nums[currentIndex] > 0 and nums[currentIndex] <= len(nums) and nums[currentIndex] != nums[correctIndex]:
      nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # perform a swap
    else:
      currentIndex += 1 # if the number at the current index is correct number, move on to next index
  
  for i in range(len(nums)):
    if nums[i] != i + 1: # the first index with wrong number is smallest missing positive number
      return i + 1 # remember to add 1 to i

  return len(nums) + 1


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))
  print(find_first_smallest_missing_positive([33, 37, 5]))


main()