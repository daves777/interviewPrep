# Problem:
# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based
# on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence
# number 4.

# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space.
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually
# an object.

# Example:
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]

# Solution:
# Since the input array contains numbers from the range 1 to n, we can use this fact to come up with an efficient way to sort the
# numbers. Since they are all unique, we cann place them at its correct place (placing 1 at index 0, 2 at index 1, and so on).
# We can do that by iterating through the array one number at a time, and if the number we are currently at is not at the correct
# index, we swap it with the number at the correct index. We can continue this process until the entire array is sorted.

# Time Complexity: O(N)
# Since we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop. But
# in worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move
# on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is equivalent to O(n).

# Space Complexity: O(1)
# We sort the array in place so we use constant space.

def cyclic_sort(nums):
  current_index = 0
  while current_index < len(nums):
    index_position = nums[current_index] - 1 # determine the index position the number should be at
    if nums[current_index] != nums[index_position]: # if the number we're looking at isn't in the position it is supposed to be
      nums[current_index], nums[index_position] = nums[index_position], nums[current_index] # swap the two numbers
    else:
      current_index += 1 # only iterate to next index if number we're looking at is in the correct index
  return nums



def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()