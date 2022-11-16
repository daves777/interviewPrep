# Problem:
# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means
# some numbers will be missing. Find all those missing numbers.

# Example:
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

# Solution:
# This problem follows the Cylic Sort pattern and is very similar to Find the Missing Number.

# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# Ignoring the space required for the output array, the algorithm uses constant space.

def find_missing_numbers(nums):
  currentIndex = 0
  while currentIndex < len(nums):
    correctIndex = nums[currentIndex] - 1 # determine the index position the number should be at
    if nums[currentIndex] != nums[correctIndex]: # if the number we're looking at is not in the correct position
      nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # swap the two numbers
    else:
      currentIndex += 1 # only iterate to the next index if number we're looking at is in the correct index
  
  missing_nums = []

  # iterate through the array again to find the missing numbers
  for i in range(len(nums)):
    if nums[i] != i + 1: # remember to add 1 to i since 2 is in nums[1], 3 is in nums[2], etc
      missing_nums.append(i + 1) # remember to add 1 to i here as well
  
  return missing_nums


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()