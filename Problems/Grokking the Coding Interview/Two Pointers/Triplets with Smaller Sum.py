# Problem:
# Given an array of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k]
# is less than target, where i, j, and k are three different indices. Write a function to return the count of
# such triplets

# Solution:
# This problem follows the two pointers pattern and shares similarities with triplet sum to zero. We need to make
# sure that each number is not used more than once.

# We can follow a similar approach by sorting the array and then iterating through one number at a time. If we
# are at number X, we need to find Y and Z such that X + Y + Z < target. At that point, the problem becomes
# finding a pair whose sum is less than target - X.

# Time Complexity: O(N^2)
# Sorting the array will take O(N*logN). The while loop within the for loop causes an N^2 computation, which
# results in O(N * logN + N^2), which is asymptotically equivalent to O(N^2)

# Space Complexity: O(N)
# The space complexity will be O(N), which is required for sorting

def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0

  for i in range(len(arr) - 2):
    target_sum = target - arr[i] # compute target sum by subtracting current index from target
    left, right = i + 1, len(arr) - 1 # set left and right pointers
    while left < right:
      if arr[left] + arr[right] < target_sum: # if pointer values less than target sum, we've found a valid triplet
        count += right - left
        # since arr[right] >= arr[left], we can replace arr[right] with any number between
        # left and right to get a sum less than the target sum
        left += 1
      else:
        right -= 1 # need a pair with smaller sum
  return count      


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()