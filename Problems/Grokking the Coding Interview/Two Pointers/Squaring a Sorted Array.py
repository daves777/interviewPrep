# Problem:
# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Solution:
# This is a simple problem, but we must account for the possibility of negative numbers in the input array. We can set left and right
# pointers at both ends of the array. After that, we can use two pointers to iterate the array. One pointer will move forward to
# iterate the negative numbers, and the other will iterate backwards to iterate the non-negative numbers. At any step, whichever
# number gives us a bigger square will be added to the output array. Once we have finished iterating the array, we can return the
# reversed array to give a sorted array from smallest to largest.

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