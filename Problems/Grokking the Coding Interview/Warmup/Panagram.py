# Problem:
# A pangram is a sentence where every letter of the English alphabet appears at least once. Given a string
# sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false
# otherwise.

# Solution:
# We can use a HashSet to check if the given sentence is a pangram or not. The HashSet will be used to store
# all the unique characters in the sentence.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of elements in the input array.
# This is because we iterate the array only once.

# Space Complexity: O(1)
# Thee space required will be O(1), because the HashSet can store at most 26 characters.

def checkIfPangram(sentence):
    letters = set()
    for letter in sentence.lower():
        if letter.isalpha():
            letters.add(letter)
    return len(letters) == 26
    

def main():
    # Expected output: True
    print(checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

    # Expected output: False
    print(checkIfPangram("This is not a pangram"))

    # Expected output: True
    print(checkIfPangram("abcdef ghijkl mnopqr stuvwxyz"))

    # Expected output: False
    print(checkIfPangram(""))

    # Expected output: True
    print(checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

main()