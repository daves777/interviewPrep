# Problem:
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the target.

# Write a function to return the indices of the two numbers such that they add up to the given target.

# Solution:
# We can follow the Two Pointers approach. We will start with one pointer pointing to the beginning of the array
# and another pointing at the end. At every step, we'll see if the numbers pointed by the two pointers add up to
# the target sum. If they do, we have found our pair; otherwise, we will do one of two things:

# 1. If the sum is greater than the target sum, decrement the end-pointer. 
# 2. If the sum is smaller than the target sum, increment the start-pointer.

# Time Complexity: O(N)
# The time complexity will be O(N) where N is the total number of elements in the given array

# Space Complexity: O(1)
# This algorithm runs in constant space

def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            return [left, right]
        
        if sum < target_sum:
            left += 1 # we need a pair with a bigger sum
        else:
            right -= 1 # we need a pair with a smaller sum
    return [-1, -1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))

main()