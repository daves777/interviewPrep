# Problem:
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal

# Solution:
# To compare the given strings, first we need to apply the backspace. It would be most efficient to do this from the end of
# both strings. We will use two seperate pointers, pointing to the last element of both strings. We can compare the characters
# pointed out by both pointers to see if the strings are equal. When one of the pointers encounters a backspace, we will skip
# and apply the backspace until we have a valid character available for comparison.

# Time Complexity: O(N)
# The time complexity will be O(M + N) where M and N are lengths of the two input strings

# Space Complexity: O(1)
# The algorithm runs in constant space

def backspace_compare(str1, str2):
  # use two pointers to compare strings
  pointer1 = len(str1) - 1
  pointer2 = len(str2) - 1
  while pointer1 >= 0 and pointer2 >= 0:
    index1 = get_next_valid_char_index(str1, pointer1)
    index2 = get_next_valid_char_index(str2, pointer2)
    if index1 < 0 and index2 < 0: # reached end of both strings
      return True
    if index1 < 0 or index2 < 0: # reached the end of one string but not the other
      return False
    if str1[index1] != str2[index2]: # if characters are not equal
      return False
    
    # iterate pointers
    pointer1 = index1 - 1
    pointer2 = index2 - 1

  return True

def get_next_valid_char_index(string, index):
  backspace_count = 0
  while index >= 0:
    if string[index] == '#': # found backspace
      backspace_count += 1
    elif backspace_count > 0: # non backspace
      backspace_count -= 1
    else: # if non backspace character and no more characters to skip from backspace count, finish search
      break
    index -= 1 # skip a character
  
  return index

def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()