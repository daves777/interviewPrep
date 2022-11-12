# Problem:
# Given a list of non-overlapping intervals sorted by their start time, insnert a given nintnerval at the correct positionn and merge all
# necessary intervals to produce a list that has only mutually exclusive intnervals

# Example:
# Intervals: [[1,3], [5,7], [8,12]], New Interval = [4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# Solution:
# If the given list was not sorted, we could have simply appended the new interval to it andn used the merge function from
# Merge Intervals. But since the given list is sorted, we can come up with a solution better thann O(N * logN)

# When we insert the interval in a sorted list, we need to find the correct index to place the interval. That means we need
# to skip the intnervals that end before the start of the new interval. (intervals[i].end < newInterval.start)

# Once we found the correct place, we can follow a similar approach as Merge Intervals to merge the new interval. We'll need
# to do something like this

# c.start = min(a.start, b.start)
# c.end = max(a.end, b.end)

# Steps:
# 1. Skip all intervals which end before the start of the new interval to determine where to place the new interval
# 2. If the new interval overlaps with the interval it is inserted next to, we need to merge them into a new interval
# 3. We will keep repeating the above two steps to merge c with the next overlapping interval

# Time Complexity: O(N)
# As we are iterating through the intervals only once, the time complexity of the above algorithm is O(N), where N is the
# total number of intervals

# Space Complexity: O(N)
# We need to return a list contnaining all of the merged intervals, so the space complexity will be O(N)

def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip all intervals that come before the new_interval
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1
  
  # merge all intervals that overlap with new_interval
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1
  
  # insert the new_interval
  merged.append(new_interval)

  # add all remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
  
  return merged


def main():
  print("Intervals after inserting the new interval: " + 
           str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + 
           str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + 
           str(insert([[2, 3], [5, 7]], [1, 4])))


main()