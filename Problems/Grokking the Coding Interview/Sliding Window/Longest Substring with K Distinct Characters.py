# Problem:
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

# We can use a hashmap to remember frequency of each character processed.

# Steps:
# 1. Insert characters from beginning of string until K distinct characters in hashmap
# 2. Remember length of window as longest window so far
# 3. Keep adding one character to sliding window in stepwise fashion
# 4. If count of distinct characters in hashmap is larger than K, shrink window from beginning until less than K
# 5. While shrinking, decrement frequency of outgoing character. If frequency becomes zero remove from hashmap
# 6. After each step check if current window length is longest so far

# Time Complexity: O(N)
# The outer for loop runs for all elements, and the inner while loop processes each element only once.
# This makes the time complexity O(N + N), which is equivalent to O(N)

# Space Complexity: O(N)
# We are storing a maximum of K + 1 characters in the hashmap

import math

def longest_substring_with_k_distinct(str1, k):
    window_start, max_length = 0, 0
    char_freq = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        
        # shrink the sliding window until K distinct characters left in char_freq
        while len(char_freq) > k:
            left_char = str1[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1 # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
    
def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()