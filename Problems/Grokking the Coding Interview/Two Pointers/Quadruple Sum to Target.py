# Problem:
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal
# to the target number.

# Solution:
# This problem uses the two pointers pattern and shares similarities with triplet sum to zero. We can iterate
# through the array, taking one number at a time. We will first sort through the array so we can avoid
# duplicates. At each step we will search for quadruplets similar to triplet sum to zero, whose sum is equal to
# the given target.

# Time Complexity: O(N^3)
# Sorting the array will take O(N*logN). Overall the solution will take O(N * logN + N^3), which is equivalent to O(N^3)

# Space Complexity: O(N)
# The space complexity will be O(N), which is required for sorting

def search_quadruplets(arr, target):
  arr.sort()
  result = []
  for i in range(len(arr) - 3):
    # skip same element to avoid duplicate quadruplets
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    for j in range(i + 1, len(arr) - 2):
      # skip same element to avoid duplicate quadruplets
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      search_pairs(arr, target, i, j, result)
  return result

def search_pairs(arr, target, first, second, result):
  left = second + 1
  right = len(arr) - 1
  while left < right:
    quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
    if quad_sum == target: # found the quadruplet
      result.append([arr[first], arr[second], arr[left], arr[right]])
      left += 1
      right -= 1
      # we can save one comparison by also iterating the right pointer because if we found a quadruplet, iterating just the left pointer guaruntees
      # the next sum will not be the same as target
      while left < right and arr[left] == arr[left - 1]:
        left += 1 # skip same element to avoid duplicate quadruplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1 # skip same element to avoid duplicate quadruplets
    elif quad_sum < target:
      left += 1 # need a pair with bigger sum
    else:
      right -= 1 # need a pair with smaller sum

def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()