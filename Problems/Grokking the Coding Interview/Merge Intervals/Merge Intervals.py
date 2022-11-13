# Problem:
# Given a list of intervals, merge all overlapping intervals to produce a list that has only mutually exclusive
# intervals.

# Example:
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

# Solution:
# This problem is asking us to merge intervals. We will accomplish that with the following steps:

# Steps:
# 1. Sort the intervals on start time to ensure a.start <= b.start
# 2. If a overlaps b (b.start <= a.end), we need to merge them into a new interval c such that
#      c.start = a.start
#      c.end = max(a.end, b.end)
# 3. We will keep repeating the above two steps to merge c with next interval if it overlaps with c

# Time Complexity: O(N*logN)
# Sorting the array takes O(N*logN), and we iterate the array once which will take O(N). Overall, this will result in a time
# complexity of O(N + N * logN), which is equivalent to O(N*logN)

# Space Complexity: O(N)
# The space required for sorting is O(N). We also need O(N) space to return a list containing all the merged intervals. This
# results in O(N + N) = O(2N), which is equivalent to O(N)

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
  if len(intervals) < 2:
    return intervals
  
  # start by sorting intervals based on start time
  intervals.sort(key=lambda x: x.start)

  result = []
  start = intervals[0].start
  end = intervals[0].end

  for i in range(1, len(intervals)): # compare interval with one in front of it
    interval = intervals[i]
    if interval.start <= end: # if next interval starts before previous end, we have overlapping interval
      end = max(interval.end, end) # adjust end of previous interval
    else:
      result.append(Interval(start, end)) # otherwise we have non-overlapping interval, add previous interval and move on to next
      start = interval.start
      end = interval.end
  
  # add the last interval
  result.append(Interval(start, end))
  return result


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()


main()