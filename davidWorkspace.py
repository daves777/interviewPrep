# Problem:
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal

def backspace_compare(str1, str2):
  pointer1 = len(str1) - 1
  pointer2 = len(str2) - 1
  while pointer1 >= 0 or pointer2 >= 0:
    index1 = get_next_valid_index(str1, pointer1)
    index2 = get_next_valid_index(str2, pointer2)
    if index1 < 0 and index2 < 0:
      return True
    elif index1 < 0 or index1 < 0:
      return False
    elif str1[index1] != str2[index2]:
      return False

    pointer1 = index1 - 1
    pointer2 = index2 - 1
  
  return True

def get_next_valid_index(string, index):
  backspace_count = 0
  while index >= 0:
    if string[index] == '#':
      backspace_count += 1
    elif backspace_count > 0:
      backspace_count -= 1
    else:
      break
    index -= 1
  return index

def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()