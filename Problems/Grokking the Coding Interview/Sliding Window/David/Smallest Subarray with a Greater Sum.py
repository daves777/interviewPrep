# Problem:
# Given an array of positive numbers and a positive number S find the length of the smallest contiguous subarray
# whose sum is greater than or equal to S. Return 0 if no such subarray exists.

# Solution:
# This is similar to Maximum Sum Subarray of size K, except the window size is not fixed.

# Steps:
# 1. Add elements from array until window sum becomes greater than or equal to S. Remember length of window as smallest window so far
# 2. Shrink window by subtracting first element until window’s sum is smaller than S again.
# 3. Check if current window length is smallest so far
# 4. Keep adding one element to sliding window in stepwise fashion

# Time Complexity: O(N)
# The outer for loop runs for all elements, and the inner while loop processes each element only once.
# This makes the time complexity O(N + N), which is equivalent to O(N)

# Space Complexity: O(1)
# We only keep track of one window sum throughout

import math

def smallest_subarray_sum(s, arr):
    window_start, window_sum, = 0, 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add next element

        # shrink window as much as possible until window_sum is smaller than s
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_length == math.inf:
        return 0
    return min_length
    
def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))

main()