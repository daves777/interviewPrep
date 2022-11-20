# Problem:
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the
# numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going
# missing. Find both these numbers.

# Example:
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.

# Solution:
# This problem follows the Cylic Sort pattern and is similar to find all duplicate numbers. We can place each number at the 
# correct index, and then iterate through the array to find the numbers not at the correct indices. Since only one number
# got corrupted, the number at the wrong index is the duplicated number, and the index itself represents the missing number

# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# We sort the array in place so we use constant space but it modifies the input array.

def find_corrupt_numbers(nums):
  currentIndex = 0
  while currentIndex < len(nums):
    correctIndex = nums[currentIndex] - 1 # determine index position the number should be at
    if nums[currentIndex] != nums[correctIndex]: # if the number at the current index is not what its supposed to be
      nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # perform a swap
    else:
      currentIndex += 1 # if the number at current index is correct number, move on to next index
  
  for i in range(len(nums)):
    if nums[i] != i + 1: # the number that is not at the correct index is a duplicate
      return [nums[i], i + 1] # the index will represent the missing number, add 1 since it is range from 1 to n
  
  else:
    return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()