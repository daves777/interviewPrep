# Problem:
# Given an array of positive numbers and a positive number S find the length of the smallest contiguous subarray
# whose sum is greater than or equal to S. Return 0 if no such subarray exists.

import math

def smallest_subarray_sum(s, arr):
    window_start, window_sum = 0, 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
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