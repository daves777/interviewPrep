# Problem:
# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each
# element appears only once. The relative order of the elements should be kept the same and you should not use
# any extra space so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving return the length of the subarray
# that has no duplicates in it.

# Solution:
# As the input array is sorted, we can shift the elements left whenever we encounter duplicates. We will keep one
# pointer for iterating the array and one pointer for placing the next non-duplicate number. So our algorithm will
# be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate
# number we’ve seen.

# Time Complexity: O(N)
# The time complexity will be O(N) where N is the total number of elements in the given array

# Space Complexity: O(1)
# This algorithm runs in constant space

def remove_duplicates(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[right] != arr[right - 1]: # if first time seeing value at right pointer
            arr[left] = arr[right] # place value at left pointer
            left += 1 # shift left pointer right one space
    return left

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()