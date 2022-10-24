# Problem:
# Given an array with positive numbers and a positive target number, find all continguous subarrays whose
# product is less than the target number

# Solution:
# This problem follows the sliding window and two pointers pattern and shares similarities with triplets with
# smaller sum. As we iterate through the array, we will use a sliding window to see the current subarray product.
# If the subarray product is greater than the target, we will shift the left pointer forwards and divide by the
# left value to reduce the product. Once a valid subarray is found with product less than target, we will add
# all combinations of subarrays from right to left.

# Time Complexity: O(N^3)
# The main for loop takes O(N), but creating subarrays can take up to O(N^2). Therefore, the overall algorithm
# will take O(N^2*N) which is O(N^3)

# Space Complexity:

from collections import deque

def find_subarrays(arr, target):
  product = 1
  left = 0
  result = []

  for right in range(len(arr)):
    # calculate product so far to add to subarray
    product *= arr[right]
    # while the product is greater than target, shift left pointer forwards until product is smaller
    while product >= target and left <= right:
      product /= arr[left]
      left += 1
    # use deque instead of list so we can append left and do so in O(1) time. This is not necessary, but makes
    # resulting subarrays more intuitive to read
    subarray = deque()
    for i in range(right, left - 1, -1): # iterate through subarray from right to left, adding all combinations
      subarray.appendleft(arr[i])
      result.append(list(subarray))
  
  return result

# This is the same problem but if it asks for number of subarrays rather than returning the actual subarrays
def find_subarrays_num(arr, target):
  product = 1
  left = 0
  result = 0

  for right in range(len(arr)):
    # calculate product so far to add to subarray
    product *= arr[right]
    # while the product is greater than target, shift left pointer forwards until product is smaller
    while product >= target and left <= right:
      product /= arr[left]
      left += 1
    result += right - left + 1  # return number of subarrays. if right and left pointers are the same, the current
                                # index counts as subarray so we need to add 1
  
  return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))
  print(find_subarrays_num([2, 5, 3, 10], 30))
  print(find_subarrays_num([8, 2, 6, 5], 50))


main()