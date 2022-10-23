# Problem:
# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each
# element appears only once. The relative order of the elements should be kept the same and you should not use
# any extra space so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving return the length of the subarray
# that has no duplicates in it.

# Solution:
# Set left and right pointers at both ends of the array, comparing the square to see which is larger. Append the
# larger of the two and shift the pointer, continuing until the entire array has been appended. Since we appended
# starting with the largest number, we will return the reversed array

# Time Complexity: O(N)
# This will only take O(N) because we are iterating the input array only once

# Space Complexity: O(N)
# The space complexity will be O(N), which will be used for the output array

def make_squares(arr):
  result = []
  left, right = 0, len(arr) - 1 # set left and right pointers
  while left <= right:
    if arr[left] * arr[left] > arr[right] * arr[right]: # if left square is greater than right square
      result.append(arr[left] * arr[left]) # add left square
      left += 1 # shift left pointer
    else: # if left square is greater than right square
      result.append(arr[right] * arr[right]) # add right square
      right -= 1 # shift right pointer
  
  return result[::-1] # return reversed array

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()