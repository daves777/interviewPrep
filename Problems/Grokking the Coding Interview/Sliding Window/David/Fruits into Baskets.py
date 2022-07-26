# Problem:
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You are given two baskets. Your goal is to pick as many fruits as possible to be placed in the given baskets.
# You are given an array of characters where each character represents a fruit tree. These are the rules:

# 1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2. You can start with any tree, but you can’t skip a tree once you have started.
# 3. You will pick exactly one fruit from every tree until you cannot (Stop when you have to pick a third fruit type)

# Write a function to return the maximum number of fruits in both baskets.

# This is similar to Longest Substring with K Distinct Characters, where K = 2

# Steps:
# 1. Insert characters from beginning of string until 2 distinct characters in hashmap
# 2. Remember length of window as longest window so far
# 3. Keep adding one character to sliding window in stepwise fashion
# 4. If count of distinct characters in hashmap is larger than 2, shrink window from beginning until less than 2
# 5. While shrinking, decrement frequency of outgoing character. If frequency becomes zero remove from hashmap
# 6. After each step check if current window length is longest so far

# Time Complexity: O(N)
# The outer for loop runs for all elements, and the inner while loop processes each element only once.
# This makes the time complexity O(N + N), which is equivalent to O(N)

# Space Complexity: O(1)
# There can be a maximum of 3 types of fruits in the hashmap

def fruits_into_baskets(fruits):
    window_start, max_length = 0, 0
    fruit_freq = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        # shrink the sliding window, until we are left with 2 fruits in fruit_freq
        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1 # shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length
    
def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()