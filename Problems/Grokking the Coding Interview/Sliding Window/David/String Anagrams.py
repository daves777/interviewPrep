# Problem:
# Given a string and a pattern, find all anagrams of the pattern in the given string.
# Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding
# permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters
# 
# For example, here are the six anagrams of the string “abc”:
# 1. abc
# 2. acb
# 3. bac
# 4. bca
# 5. cab
# 6. cba

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Solution:
# This is very similar to Permutation in a String. We need to find every occurence of any permutation of the pattern
# in the string. We can use a list to store the starting indices of the anagrams of the pattern in the string

# Steps:
# 1. Create HashMap to calculate frequencies of all characters in pattern
# 2. Iterate through string, adding one character at a time to sliding window
# 3. If added character matches a character in hashmap, decrement its frequency in hashmap. If character frequency becomes zero, we got a match for that character
# 4. If number of characters matched is equal to number of distinct characters in pattern we have gotten our required permutation, so add index of start of window
# 5. If window size is greater than length of pattern, shrink window to match pattern’s size. If outgoing character is part of pattern, insert back in the frequency HashMap.

# Time Complexity: O(N)
# The time complexity is O(N + M), where N and M are the number of characters in the input string and the pattern, respectively

# Space Complexity: O(N)
# In the worst case, the whole pattern can have distinct characters that will go into the hashmap

def find_string_anagrams(str1, pattern):
    window_start, matches = 0, 0
    indices = []
    char_freq = {}

    # Setup frequency hashmap using pattern
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    
    # Goal is to match all characters from char_freq with current window
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            # Decrement frequency of matched character
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matches += 1
        
        if matches == len(char_freq): # Have we found an anagram
            indices.append(window_start)
        
        # Shrink the sliding window
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matches -= 1 # Before putting the character back, decrement the matches count
                char_freq[left_char] += 1 # put character back
    
    return indices

def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))

main()