# Problem:
# Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k

# We can use a HashMap to remember the frequencies of all characters in the given pattern.
# Our goal will be to match all the characters from this HashMap with a sliding window in the given string.

# Steps:
# 1. Create HashMap to calculate frequencies of all characters in pattern
# 2. Iterate through string, adding one character at a time to sliding window
# 3. If added character matches a character in hashmap, decrement its frequency in hashmap. If character frequency becomes zero, we got a match for that character
# 4. If number of characters matched is equal to number of distinct characters in pattern we have gotten our required permutation
# 5. If window size is greater than length of pattern, shrink window to match pattern’s size. If outgoing character is part of pattern, insert back in the frequency HashMap.

# Time Complexity: O(N)
# The time complexity is O(N + M), where N and M are the number of characters in the input string and the pattern, respectively

# Space Complexity: O(N)
# In the worst case, the whole pattern can have distinct characters that will go into the hashmap

def find_permutation(str1, pattern):
    window_start, matches = 0, 0
    char_freq = {}

    # Setup frequency hashmap using pattern
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    
    # Goal is to match all the characters from the 'char_freq' with the current window
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            # decrement the frequency of matched character
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matches += 1
        
        # If number of matches is the same as number of distinct characters in hashmap, permutation exists
        if matches == len(char_freq):
            return True
        
        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matches -= 1
                char_freq[left_char] += 1

    # If matches never reaches desired number, permutation does not exist
    return False
    
def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()