# Problem:
# Given a string with lowercase letters, if you are can replace no more than k letters with any letter
# find the length of the longest substring having the same letters after replacement.

# We can use a hashmap to remember the frequency of each letter

# Steps:
# 1. Iterate through the string to add one letter at a time in the window
# 2. Keep track of the count of maximum repeating letter in any window maxRepeatLetterCount
# 4. Within the window a letter repeats maxRepeatLetterCount times, we should try to replace the remaining
# 5. If remaining letters are less than or equal to k, we can replace them all
# 6. If we have more than k remaining letters, shrink the window as we cannot replace more than k letters

# Time Complexity: O(N)
# Where N is the number of characters in the input string

# Space Complexity: O(1)
# We expect only lowercase letters in input string, so space complexity will be O(26) to store each
# letter's frequency in the hashmap, which is asymptotically equal to O(1)

def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    char_freq = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[right_char])

        # Current window size is from window_start to window_end, overall we have a letter 
        # which is repeating 'max_repeat_letter_count' times, this means we can have a window 
        # which has one letter repeating 'max_repeat_letter_count' times and the remaining 
        # letters we should replace. If the remaining letters are more than 'k', it is the 
        # time to shrink the window as we are not allowed to replace more than 'k' letters   
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            char_freq[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length
    
def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))

main()