# Problem:
# Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str1):
    window_start, max_length = 0, 0
    chars = set()
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        while(right_char in chars):
            left_char = str1[window_start]
            window_start += 1
            chars.remove(left_char)
        chars.add(right_char)
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

    
def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    print("Length of the longest substring: " + str(non_repeat_substring("cabaaccbb")))

main()