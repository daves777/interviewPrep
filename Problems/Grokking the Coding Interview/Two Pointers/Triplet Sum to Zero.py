# Problem:
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Solution:
# This problem follows the two pointers pattern and is similar to Pair with Target Sum. The difference is that the
# input array is not sorted and instead of a pair we need to find triplets with a target sum of zero. To solve
# this, first we will sort through the array and then iterate one number at a time. Once we find number X, we need
# to find Y and Z such that X + Y + Z = 0. At that point, it becomes a problem of finding a pair whose sum is
# equal to -X. We will also need to find only unique triplets, so we'll have to skip duplicate numbers. This will
# be easier since the duplicates will be next to each other after the array is sorted.

# Time Complexity: O(N^2)
# Sorting the array will take O(N*logN). Overall, the function will take O(N * logN + N^2), which is asymptotically
# equivalent to O(N^2)

# Space Complexity: O(N)
# Ignoring the space required for output array, the space complexity will be O(N), which is required for sorting

def search_triplets(arr):
  result = []
  arr.sort() # sort array to avoid duplicates more easily

  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i - 1]: # if index is duplicate, skip
      continue

    left, right = i + 1, len(arr) - 1 # set left and right pointers
    while left < right:
      sum = arr[i] + arr[left] + arr[right] # compute sum
      if sum > 0: # if sum is greater than zero, decrease right pointer
        right -= 1
      elif sum < 0: # if sum is less than zero, increase left pointer
        left += 1
      else: # if sum is equal to zero
        result.append([arr[i], arr[left], arr[right]]) # append triplet to result
        left += 1 # shift left pointer
        while arr[left] == arr[left - 1] and left < right: # if left pointer is duplicate, keep skipping
          left += 1
  
  return result


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()