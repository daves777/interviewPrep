# Problem:
# Given an unsorted array containing numbers and a number 'k', find the first 'k' missing positive numbers in the array

# Example:
# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.

# Solution:
# This problem follows the Cylic Sort pattern and is similar to find the smallest missing positive number. Following a similar approach,
# we will place the numbers on their correct indices and ignore numbers that are out of range of the array. Once finished with the cyclic
# sort, we will iterate the array to find indices that do not have correct numbers. # If we cannot find 'k' missing numbers from the
# array, we'll need to add numbers to the output array. We can use the length of the array to find the additional numbers. One tricky 
# part is that the additional numbers could already be part of the array, since we ignored numbers while iterating the array. So we must
# keep track of all numbers from those indices that have missing numbers.

# Time Complexity: O(N)
# The first while will run for O(N), and the last two for loops will run for O(N) and O(k) respectively. This results in a runtime of O(N)
# because it is based off of the input

# Space Complexity: O(N)
# We will need O(k) space to store the extraNumbers

def find_first_k_missing_positive(nums, k):
  currentIndex = 0
  while currentIndex < len(nums):
    correctIndex = nums[currentIndex] - 1 # determine index position the number should be at
    # if number is valid (positive number less than length of array) and number at current index is not correct
    if nums[currentIndex] > 0 and nums[currentIndex] <= len(nums) and nums[currentIndex] != nums[correctIndex]:
      nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # perform a swap
    else:
      currentIndex += 1 # if the number at the current index is correct number, move on to next index
  
  missingNumbers = [] # array to hold final list of missing numbers
  extraNumbers = set() # set to hold any extra numbers in the array nums

  for i in range(len(nums)): # iterate the array again
    if len(missingNumbers) < k: # while we don't have the required number of missing k numbers
      if nums[i] != i + 1: # if number at current index is not the expected number
        missingNumbers.append(i + 1) # add the expected number to missing numbers
        extraNumbers.add(nums[i]) # add actual number to extra numbers

  i = 1
  while len(missingNumbers) < k: # while we don't have the required number of missing k numbers
    currentNumber = i + len(nums) # calculate current number
    if currentNumber not in extraNumbers: # if current number isn't already in extra numbers
      missingNumbers.append(currentNumber) # add current number to missing numbers
    i += 1
  
  return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()