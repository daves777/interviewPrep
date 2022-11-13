# Problem:
# Given a list of intervals representing the start and end time of 'N' meetings, find the minimum number of rooms required to 
# hold all the meetings

# Example:
# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
# occur in any of the two rooms later.

# Solution:
# This problem follows the merge intervals pattern. We can sort the intervals by start time, and use a similar approach as
# Merge Intervals to determine the rooms required. We need to keep track of the ending time of all the meetings currently happening
# so that when we try to schedule a new meeting, we can see what meetings have already ended. A good data structure for this would
# be a Minimum Heap.

# Strategy:
# 1. Sort the meetings based on start time
# 2. Schedule the first meeting(m1) in one room(r1)
# 3. If the next meeting m2 is not overlapping with m1, we can schedule it in the same room r1
# 4. If the next meeting m3 is overlapping with m2 we can't use r1, so we will schedule it in another room(r2)
# 5. Now if the next meeting m4 is overlapping with m3, we need to see if room r1 has become free. To do this, we need to 
#    keep track of the end time of the meeting happening in it. If the end time of m2 is before the start time of m4, we can
#    use that room r1. Otherwise, we need to schedule m4 in another room r3

# Steps:
# 1. Sort the meetings based on start time
# 2. Create a min-heap to store all active meetings. This min-heap will be used to find active meeting with smallest end time.
# 3. Iterate through all meetings one by one to add them to the min-heap. Let's say we are trying to schedule meeting m1
# 4. Since the min-heap contains all the active meetings, before scheduling m1 we can remove all meetings from the heap that
#    have an end time smaller than or equal to start time of m1
# 5. Add m1 to the heap
# 6. The heap will always have all the overlapping meetings, so we will need rooms for all of them. Keep a counter to remember
#    maximum size of the heap at any time which will be the minimum number of rooms needed.

# Time Complexity: O(N)
# We are sorting the intervals, which will take O(N*logN). While iterating the meetings, we use heap actions that could take up
# to O(logN) time. This equates to O(N*logN + logN) which is equivalent to O(N*logN)

# Space Complexity: O(N)
# THe space complexity required for sorting is O(N). In the worst case, we have to insert all meetings into the min heap, which
# can take up to O(N) space. This results in O(N + N), which is equivalent to O(N) space.

from heapq import *

class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __lt__(self, other):
    # min heap based on meeting.end
    return self.end < other.end


def min_meeting_rooms(meetings):
  # sort list based on meeting start time
  meetings.sort(key = lambda x: x.start)

  minRooms = 0
  rooms = []

  # iterate through meetings
  for meeting in meetings:
    # if room at top of heap has meeting end time before the current meeting start time
    while len(rooms) > 0 and meeting.start >= rooms[0].end:
      # pop room from heap
      heappop(rooms)
    # add current meeting into a room in the heap
    heappush(rooms, meeting)
    # keep track of max number of rooms needed
    minRooms = max(minRooms, len(rooms))
  
  return minRooms


def main():
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()