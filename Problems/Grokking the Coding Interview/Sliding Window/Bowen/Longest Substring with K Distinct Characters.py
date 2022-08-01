# Problem:
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

def longest_substring_with_k_distinct(str1, k):
    length = 0
    chars = dict()
    left = 0
    for i in range(len(str1)):
        char = str1[i]
        if(char not in chars):
            chars[char] = 0
        chars[char] = chars[char]+1
        while(len(chars)>k):
            leftChar = str1[left]
            chars[leftChar] = chars[leftChar] -1
            if(chars[leftChar]==0):
                chars.pop(leftChar)
            left+=1
        length = max(length,i-left+1)
    return length


        
    
def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()