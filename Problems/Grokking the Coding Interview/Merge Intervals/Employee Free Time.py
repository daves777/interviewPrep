# Problem:
# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if
# there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted
# on the start time.

# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: Both employees are free between [3,5].

# Solution:
# This problem follows the merge intervals pattern. We can solve it by doing the following:

# Steps:
# 1. Sort intervals by start time
# 2. Merge overlapping busy intervals
# 3. Find time between intervals

# Time Complexity: O(N^2)
# We flatten the intervals first, which uses a nested for loop. This results in O(N^2). We are also sorting the intervals,
# which will take O(N*logN). This equates to O(N*logN + N^2) which is equivalent to O(N^2)

# Space Complexity: O(N)
# The space complexity required for sorting is O(N). We also need O(N) space for the resulting array. This results in a
# space complexity of O(N + N) which is equivalent to O(N)

class Interval:
  def __init__(self, start, end):
      self.start = start
      self.end = end

  def print_interval(self):
      print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def find_employee_free_time(schedule):
  intervals = []

  # flatten given intervals into one big list
  for i in schedule:
    for j in i:
      intervals.append(j)
  
  # sort all the intervals by their starting time
  intervals.sort(key = lambda x : x.start)

  # merge all overlapping intervals
  merged = []
  start = intervals[0].start
  end = intervals[0].end

  for i in range(1, len(intervals)): # compare interval with one in front of it
    interval = intervals[i]
    if interval.start <= end: # if next interval starts before previous ends, we have overlapping interval
      end = max(interval.end, end) # adjust end of previous interval
    else:
      merged.append(Interval(start, end)) # otherwise we have non-overlapping interval, add previous interval and move on to next
      start = interval.start
      end = interval.end
      
  # remember to add last interval
  merged.append(Interval(start, end))

  # create free intervals using time between merged intervals. We can use end and start times of intervals to find this
  free = []
  for i in range(1, len(merged)):
    free.append(Interval(merged[i - 1].end, merged[i].start))
  
  return free


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()