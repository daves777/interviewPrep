# Problem:
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but
# it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to
# modify the input array

# Example:
# Input: [1, 4, 4, 3, 2]
# Output: 4

# Solution:
# This problem follows the Cylic Sort pattern and is similar to find the missing number. We will first try to place each number
# at the correct index. Since there is only one duplicate, if while swapping the number with its index both the numbers being
# swapped are the same, we have found the duplicate.


# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# We sort the array in place so we use constant space but it modifies the input array.

def find_duplicate(nums):
  currentIndex = 0
  while currentIndex < len(nums):
    if nums[currentIndex] != currentIndex + 1: # if the number at the current index is not what its supposed to be (index + 1)
      correctIndex = nums[currentIndex] - 1 # determine index position the number should be at
      if nums[currentIndex] != nums[correctIndex]: # if the two numbers are not the same
        nums[currentIndex], nums[correctIndex] = nums[correctIndex], nums[currentIndex] # perform a swap
      else:
        # if it has reached this point, the number at the current index is not the correct number according to the index, and a
        # swap was attempted where the two numbers were the same, so this must be our duplicate
        return nums[currentIndex]
    else: # if the number at current index is correct number, move on to next index
      currentIndex += 1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()