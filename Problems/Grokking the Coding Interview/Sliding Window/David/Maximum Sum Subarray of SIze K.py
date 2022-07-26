# Problem:
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# To calculate the sum of a contiguous subarray, utilize the sum of the previous subarray.

# Steps:
# 1. Subtract element going out of sliding window (first element of the window)
# 2. Add next element to sliding window (the element right after the end of the window)

# Time Complexity: O(N)

# Space Complexity: O(1)
# We only keep track of one sum, and the length of sliding window remain the same throughout

def max_sub_array_of_size_k(k, arr):
    window_start, window_sum, max_sum = 0, 0, 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element
        # if the window size has hit size k, slide right
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # subtract element going out
            window_start += 1 # slide window ahead

    return max_sum
    
def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()