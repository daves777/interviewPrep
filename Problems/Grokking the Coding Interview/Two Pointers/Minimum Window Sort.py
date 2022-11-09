# Problem:
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Solution:
# To find the smallest subarray, we can use the two pointers approach starting at the begining and end of the array moving
# inwnards to find elements out of order. However, we must also consider elements within the subarray that could be smaller
# than the maximum or larger than the minimum of the subarray

# Steps:
# 1. From the beginning and end of the array, find the first elements that are out of the sorting order. This will create the candidate subarray
# 2. Find the max and min of this subarray
# 3. Extend subarray from beginning to include any number bigger than the minimum of the subarray
# 4. Extend subarray from end to include any number smaller than the maximum of the subarray

# Time Complexity: O(N)
# The time complexity will be O(N)

# Space Complexity: O(1)
# The algorithm runs in constant space

def shortest_window_sort(arr):
  low, high = 0, len(arr) - 1
  # find the first number out of order from beginning
  while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
    low += 1

  if low == len(arr) - 1: # if we've reached the end without stopping the array is already sorted
    return 0
  
  # find the first number out of order from end
  while high > 1 and arr[high] >= arr[high - 1]:
    high -= 1
  
  # find max and min of subarray
  subarray_max = max(arr[low:high])
  subarray_min = min(arr[low:high])
  
  # extend subarray left to include numbers larger than min
  while low > 0 and arr[low - 1] > subarray_min:
    low -= 1
  # extend subarray right to include numbers smaller than max
  while high < len(arr) - 1 and arr[high + 1] < subarray_max:
    high += 1
  
  return high - low + 1

def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))


main()