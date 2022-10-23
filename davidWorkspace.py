# Problem:
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to
# target number as possible, return the sum of the triplet. If there are more than one such triplet, return the
# sum of the triplet with the smallest sum

import math

def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_diff = math.inf

  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i - 1]:
      continue

    left, right = i + 1, len(arr) - 1
    while left < right:
      current_diff = target_sum - arr[i] - arr[left] - arr[right]
      if current_diff == 0:
        return target_sum
      elif abs(current_diff) < abs(smallest_diff) or abs(current_diff) == abs(smallest_diff) and current_diff > 0:
        smallest_diff = current_diff
      if current_diff > 0:
        left += 1
      else:
        right -= 1
  
  return target_sum - smallest_diff


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
  print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))
  print(triplet_sum_close_to_target([1, 1, 1, 0], 100))


main()