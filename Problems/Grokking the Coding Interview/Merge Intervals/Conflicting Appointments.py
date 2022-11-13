# Problem:
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example:
# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# Solution:
# This problem follows the merge intervals pattern. We can sort the intervals by start time, and use a similar approach as
# Merge Intervals to determine if there are any overlap between intervals.

# Time Complexity: O(N*logN)
# We are sorting the intervals, which will take O(N*logN). We iterating through the intervals only once, so the overall time
# complexity is O(N + N*logN), which is equivalent to O(N*logN)

# Space Complexity: O(N)
# The space complexity will be O(N), since that is the space required for sorting.

def can_attend_all_appointments(intervals):
  # sort by start time
  intervals.sort(key = lambda x: x[0])
  start, end = 0, 1
  # iterate through intervals starting with second interval and comparing back
  for i in range(1, len(intervals)):
    # if second interval start is before previous interval end, there is a conflict
    if intervals[i][start] < intervals[i - 1][end]:
      return False
  return True


def main():
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()