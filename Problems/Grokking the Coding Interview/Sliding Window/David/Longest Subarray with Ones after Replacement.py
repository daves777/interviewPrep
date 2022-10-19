# Problem:
# Given an array containing 0s and 1s, if you can replace no more than k 0s with 1s, find the length of the longest
# contiguous subarray having all 1s

# Solution:
# We can iterate through the array keeping track of the maximum number of 1s in the window. If we have more than
# k remaining 0s, we will shrink the window as we cannot replace more than k 0s

# Steps:
# 1. Iterate through the string to add one 1 at a time in the window
# 2. Keep track of the count of maximum repeating 1s in any window maxOnesCount
# 4. Within the window a 1 repeats maxOnesCount times, we should try to replace the remaining numbers
# 5. If remaining numbers are less than or equal to k, we can replace them all
# 6. If we have more than k remaining 0s, shrink the window as we cannot replace more than k 0s

# Time Complexity: O(N)
# Where N is the count of numbers in the input array

# Space Complexity: O(1)

def length_of_longest_substring(arr, k):
    window_start, max_length, maxOnesCount = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        right_num = arr[window_end]
        if right_num == 1:
            maxOnesCount += 1
        
        # Current window size is from window_start to window_end, overall we have a maximum 
        # of 1s repeating 'max_ones_count' times, this means we can have a window with 
        # 'max_ones_count' 1s and the remaining are 0s which should replace with 1s.
        # Now, if the remaining 0s are more than 'k', it is the time to shrink the window as
        # we are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - maxOnesCount) > k:
            left_num = arr[window_start]
            if left_num == 1:
                maxOnesCount -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()