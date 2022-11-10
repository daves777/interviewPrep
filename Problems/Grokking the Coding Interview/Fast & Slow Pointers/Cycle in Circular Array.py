# Problem:
# We are given an array containing positive and negative numbers. Suppose the array contains a number 'M' at a particular index
# If 'M' is positive, we will move forward 'M' indices and if 'M' is negative move backwards 'M' indices. You should assume
# that the array is circular which means two things:

# 1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement
# 2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement

# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one
# direction, which means the cycle should not contain both forward and backward movements

# Solution:
# This problem involves finding a cycle in the array, and we can use the Fast & Slow Pointer method to do that. We can start
# from each index of the array to find the cycle. If a number does not have a cycle, we will move forward to the next element.

# 1. The cycle should have more than one element. This means if we move a pointer forward and end up at the same element, we
# have a one element cycle. Thus, we can finish the cycle search for the current element.

# 2. The cycle cannot have both forward and backward movemeents. If we remember the direction of each element while searching
# for the cycle, when we encounter a change in direction we can finish our cycle search for that element.

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

def circular_array_loop_exists(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0 # if we are moving forward or not
    slow, fast = i, i

    # if slow or fast becomes -1, this means we cannot find the cycle for this number
    while True:
      # move one step for slow pointer
      slow = find_next_index(arr, is_forward, slow)
      # move one step for fast pointer
      fast = find_next_index(arr, is_forward, fast)
      if fast != -1:
        # if fast pointer is valid, move another step
        fast = find_next_index(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break
    
    # if slow and fast are valid and the same, we have found a cycle
    if slow != -1 and slow == fast:
      return True
    
  return False

def find_next_index(arr, is_forward, current_index):
  direction = arr[current_index] >= 0

  if is_forward != direction: # change in direction, return -1
    return -1
  
  next_index = (current_index + arr[current_index]) % len(arr)

  if next_index == current_index: # one element cycle, return -1
    return -1
  
  return next_index


def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()
