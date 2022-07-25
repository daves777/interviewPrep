# Problem:
# Given a string and a pattern, find the smallest substring in the given string which has all the character
# occurrences of the given pattern.

# Steps:
# 1. Create HashMap to calculate frequencies of all characters in pattern
# 2. Iterate through string, adding one character at a time to sliding window
# 3. If added character matches a character in hashmap, decrement its frequency in hashmap. While character frequency is more than zero, we got a match for that character
# 4. If number of characters matched is equal to number of distinct characters in pattern we have gotten our pattern
# 5. While substring contains all letters in pattern, shrink window from left. If outgoing character is part of pattern, insert back in the frequency HashMap.

# Time Complexity: O(N)
# The time complexity is O(N + M), where N and M are the number of characters in the input string and the pattern, respectively

# Space Complexity: O(N)
# In the worst case, the whole pattern can have distinct characters that will go into the hashmap

def find_substring(str1, pattern):
    window_start, matches, substring_start = 0, 0, 0
    min_length = len(str1) + 1
    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] >= 0: # Count match of a character if frequency more than 1
                matches += 1
        
        # Shrink the window from left until window no longer contains all matched characters
        while matches == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substring_start = window_start
            
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_freq:
                # we could have redundant matching characters, so we need to
                # decrement the matched count only when a useful occurrence of a matched
                # character is going out of the window, so when frequency goes from negative to 0
                if char_freq[left_char] == 0:
                    matches -= 1
                char_freq[left_char] += 1
    
    if min_length > len(str1):
        return ""
    return str1[substring_start:substring_start + min_length]

def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))

main()