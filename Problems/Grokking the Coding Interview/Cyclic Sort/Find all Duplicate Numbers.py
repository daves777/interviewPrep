# Problem:
# We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice,
# find all these duplicate numbers using constant space.

# Example:
# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]

# Solution:
# This problem follows the Cylic Sort pattern and is similar to find the duplicate number. We can place each number at the 
# correct index, and then iterate through the array to find all numbers not at the correct indices. These numbers are the 
# duplicates.

# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# We sort the array in place so we use constant space but it modifies the input array.

def find_all_duplicates(nums):
  currentIndex = 0
  while currentIndex < len(nums):
    correctIndex = nums[currentIndex] - 1 # determine index position the number should be at
    if nums[currentIndex] != nums[correctIndex]: # if the number at the current index is not what its supposed to be
      nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # perform a swap
    else:
      currentIndex += 1 # if the number at current index is correct number, move on to next index
  
  duplicates = []

  for i in range(len(nums)):
    if nums[i] != i + 1: # any number that is not at the correct index is a duplicate
      duplicates.append(nums[i])
  
  return duplicates


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()