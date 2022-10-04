# Problem:
# Given a string and list of words, find all starting indices of substrings in the given string that
# are a concatenation of all given words exactly once without any overlapping of words. It is given
# that all words are of the same length

# This problem is similar to maximum sum subarray of size k. We will keep track of all the words
# with a hashmap and try to match them in the given string.

# Steps:
# 1. Keep the frequency of every word in a hashmap
# 2. Starting from every index in the string, try to match all the words
# 4. In each iteration, keep track of all the words we have already seen in another hashmap
# 5. If a word is not found or has a higher frequency than required, move to next character
# 6. Store the index if all words found

# Time Complexity: O(N * M * Len)
# Where N is the number of characters in the string, M is the total number of words, and Len
# is the length of a word

# Space Complexity: O(N)
# At most, we will be storing all the words in the two hashmaps. In worst case, we need O(N) space
# for the resulting list, so O(M + N)

def find_word_concatenation(str1, words):
    # if words is empty or length of first word is 0
    if len(words) == 0 or len(words[0]) == 0:
        return []

    # keep track of number of words, word length, and word frequency
    words_count = len(words)
    word_length = len(words[0])
    word_freq = {}
    result = []

    # create word frequency hashmap
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
    # iterate through string by length of substring
    for i in range(0, (len(str1) - words_count * word_length) + 1, word_length):
        # keep track of words seen
        words_seen = {}
        # iterate through words within substring based on number of words in substring
        for j in range(0, words_count):
            # find index of next word
            next_word_index = i + j * word_length
            # get the next word from string
            word = str1[next_word_index:next_word_index + word_length]
            #break if we don't need this word
            if word not in word_freq:
                break
            # add word to the words seen hashmap
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1
            # no need to continue if word has higher frequency than required
            if words_seen[word] > word_freq[word]:
                break
            if j + 1 == words_count: # store index if all words found
                result.append(i)
    return result
    
def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
    print(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

main()