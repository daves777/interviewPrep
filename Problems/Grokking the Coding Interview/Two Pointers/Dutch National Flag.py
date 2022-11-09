# Problem:
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

# Solution:
# We can use a two pointers approach while iterating through the array. Set a low and high pointer pointing to
# the first and last element of the array respectively. While iterating, we move all the 0s before low and all
# the 2s after high so that in the end, all 1s will be between low and high

# Time Complexity: O(N)
# The time complexity of the above algorithm will be O(N) as we are iterating the input array only once

# Space Complexity: O(1)
# We do not create any new arrays or use up any additional space since this is an in place sort, so the algorithm runs in constant space O(1)

def dutch_flag_sort(arr):
  # all elements < low are 0, all elements > high are 2
  # all elements >= low < i are 1
  low, high = 0, len(arr) - 1
  i = 0
  while i <= high:
    if arr[i] == 0:
      # swap elements at position i and low
      arr[i], arr[low] = arr[low], arr[i]
      # increment i and low
      low += 1
      i += 1
    elif arr[i] == 1:
      # if encountered 1, just continue since it will remain in the middle
      i += 1
    # else if element is 2
    else:
      # swap elements at position i and high
      arr[i], arr[high] = arr[high], arr[i]
      #only decrement high, since we just swapped i and it could be a 0, 1, or 2
      high -= 1

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)

main()