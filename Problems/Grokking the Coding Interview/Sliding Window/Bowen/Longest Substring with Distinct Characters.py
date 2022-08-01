# Problem:
# Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str1):
    indices = dict()
    currLength=0
    maxLength = 0
    maxIndice = 0
    for i in range(len(str1)):
        char = str1[i]
        if char in indices:
            maxLength  = max(maxLength,currLength)
            maxIndice = max(maxIndice,indices[char])
            currLength = i - maxIndice
        else:
            currLength+=1
        indices[char] = i
    return max(maxLength,currLength)

def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    print("Length of the longest substring: " + str(non_repeat_substring("aabaaccbb")))

main()