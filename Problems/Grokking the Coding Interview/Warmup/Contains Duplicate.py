# Problem:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct.

# Solution:
# We can use the set data structure to check for duplicates in an array. Since a set can only hold unique elements,
# we can check if the elements in the given array are present more than once by adding them to a set. This way,
# we can determine if there are any duplicates in the array.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of elements in the input array.
# This is because we iterate the array only once.

# Space Complexity: O(N)
# Thee space required will be O(N), as it stores the numbers in a set

def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False
    

def main():
    nums1 = [1, 2, 3, 4]
    print(containsDuplicate(nums1)) # Expected output: False

    nums2 = [1, 2, 3, 1]
    print(containsDuplicate(nums2)) # Expected output: True

    nums3 = []
    print(containsDuplicate(nums3)) # Expected output: False

    nums4 = [1, 1, 1, 1]
    print(containsDuplicate(nums4)) # Expected output: True

main()