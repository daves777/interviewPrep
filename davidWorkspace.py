# Problem:
# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each
# element appears only once. The relative order of the elements should be kept the same and you should not use
# any extra space so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving return the length of the subarray
# that has no duplicates in it.

def make_squares(arr):
  result = []
  left, right = 0, len(arr) - 1
  while left <= right:
    if arr[left] * arr[left] > arr[right] * arr[right]:
      result.append(arr[left] * arr[left])
      left += 1
    else:
      result.append(arr[right] * arr[right])
      right -= 1
  
  return result[::-1]

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()