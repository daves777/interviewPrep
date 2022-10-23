# Problem:
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to
# target number as possible, return the sum of the triplet. If there are more than one such triplet, return the
# sum of the triplet with the smallest sum

# Solution:
# This problem is similar to Triplet Sum to Zero. We can follow a similar approach by iterating through the array
# and keeping track of the difference between the triplet sum and target sum.

# Time Complexity: O(N^2)
# Sorting the array will take O(N*logN). Overall, the function will take O(N * logN + N^2), which is asymptotically
# equivalent to O(N^2)

# Space Complexity: O(N)
# This algorithm runs in O(N), which is required for sorting

import math

def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_diff = math.inf

  for i in range(len(arr) - 2):
    if i > 0 and arr[i] == arr[i - 1]: # skip when duplicate element
      continue

    left, right = i + 1, len(arr) - 1 # set left and right pointers
    while left < right:
      current_diff = target_sum - arr[i] - arr[left] - arr[right]
      if current_diff == 0: # if triplet with exact sum found
        return target_sum # return sum of all numbers

      # second part of if is to account for when the difference is the same, but we need the triplet with smallest
      # sum. We can determine this if the absolute value of difference is the same but current difference is
      # a positive number, meaning the target_sum is greater than the current sum. That means we are using the
      # triplet with the smaller sum
      elif abs(current_diff) < abs(smallest_diff) or abs(current_diff) == abs(smallest_diff) and current_diff > 0:
        smallest_diff = current_diff
      if current_diff > 0:
        left += 1 # need triplet with bigger sum
      else:
        right -= 1 # need triplet with smaller sum
    
  return target_sum - smallest_diff

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
  print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))


main()