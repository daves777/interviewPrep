# Problem:
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted
# on their start time.

# Example:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

# Solution:
# This problem follows the merge intervals pattern. Whenever the two intervals overlap, one of the interval's start time lies
# within the other interval. This can help us identify if any two intervals overlap or not.

# Our algorithm will be to iterate through both the lists together to see if any two intervals overlap. If two intervals
# overlap, we will insert the overlapped part into a result list and move on to the next interval which is finishing early.

# Time Complexity: O(N)
# As we are iterating through both the lists only once, the time complexity of the above algorithm is O(N + M) where N and M
# are the number of intervals in the input arrays respectively.

# Space Complexity: O(N)
# We need space to return the result list, so the space complexity will be O(N)

def merge(intervals_a, intervals_b):
  result = []
  i, j, start, end = 0, 0, 0, 1

  while i < len(intervals_a) and j < len(intervals_b):
    # check if intervals_a[i]'s start time lies within the interval of intervals_b[j]
    a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end]
    # check if intervals_b[j]'s start time lies within the interval of intervals_a[i]
    b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] <= intervals_a[i][end]
    # if there is overlap, merge the intervals and append to result
    if a_overlaps_b or b_overlaps_a:
      newStart = max(intervals_a[i][start], intervals_b[j][start])
      newEnd = min(intervals_a[i][end], intervals_b[j][end])
      result.append([newStart, newEnd])

    # iterate using the interval that finished first
    if intervals_a[i][end] < intervals_b[j][end]:
      i += 1
    else:
      j += 1
  
  return result

def main():
  print("Intervals Intersection: " + 
             str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + 
             str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()