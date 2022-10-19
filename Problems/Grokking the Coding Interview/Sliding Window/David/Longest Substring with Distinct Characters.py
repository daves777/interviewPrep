# Problem:
# Given a string, find the length of the longest substring, which has all distinct characters.

# Solution:
# We can use a hashmap to remember the last index of each character processed.
# When we get duplicate characters, we shrink the sliding window to ensure we always have distinct characters

# Steps:
# 1. Insert characters from beginning of string in hashmap with their index
# 2. Remember length of window as longest window so far
# 4. If we find a duplicate character, shrink window to last index of character
# 5. While shrinking, replace index of character with new index
# 6. After each step check if current window length is longest so far

# Time Complexity: O(N)
# Where N is the number of characters in the input string

# Space Complexity: O(1)
# Space complexity will be O(K), where K is the number of distinct characters in the input string
# In worst case, the whole string might be distinct, so the entire string will be added to the hashmap
# We can expect a fixed set of characters in input string (26 letters), so the algorithm runs in fixed space O(1)

def non_repeat_substring(str1):
    window_start, max_length = 0, 0
    char_index = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the hashmap already contains right_char, shrink window from beginning so only have one occurrence
        if right_char in char_index:
            # We have to account for if window_start is already ahead of the last index of right_char
            # If window_start is ahead, keep current value instead of moving it back
            window_start = max(window_start, char_index[right_char] + 1)
        # insert right_char into map
        char_index[right_char] = window_end
        # remember the max length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
        
    
def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()