# Problem:
# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find
# the maximum CPU load at any time if all the jobs are running on the same machine.

# Jobs: [[1,4,3], [2,5,4], [7,9,6]]
# Output: 7
# Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
# jobs are running at the same time i.e., during the time interval (2,4).

# Solution:
# This problem follows the merge intervals pattern, and can be converted into Minimum Meeting Rooms. Similar to Minimum
# Meeting Rooms where we were trying to find the maximum number of meetings, for this problem we are trying to find the
# maximum number of jobs running at any time. We will need to keep a running count of the maximum CPU load at any time to
# find the overall maximum load.

# Time Complexity: O(N)
# We are sorting the intervals, which will take O(N*logN). While iterating the jobs, we use heap actions that could take up
# to O(logN) time. This equates to O(N*logN + logN) which is equivalent to O(N*logN)

# Space Complexity: O(N)
# THe space complexity required for sorting is O(N). In the worst case, we have to insert all jobs into the min heap, which
# can take up to O(N) space. This results in O(N + N), which is equivalent to O(N) space.

from heapq import *

class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

  def __lt__(self, other):
    # min heap based on job.end
    return self.end < other.end


def find_max_cpu_load(jobs):
  # sort jobs by start time
  jobs.sort(key = lambda x: x.start)
  max_cpu_load, current_cpu_load = 0, 0
  min_heap = []

  # iterate through jobs
  for job in jobs:
    # if job at top of heap has end time before current job start time
    while len(min_heap) > 0 and job.start >= min_heap[0].end:
      # adjust current cpu_load
      current_cpu_load -= min_heap[0].cpu_load
      # pop job from heap
      heappop(min_heap)
    # add current job into heap
    heappush(min_heap, job)
    # adjust current cpu_load
    current_cpu_load += job.cpu_load
    # keep track of max cpu_load
    max_cpu_load = max(max_cpu_load, current_cpu_load)
  
  return max_cpu_load


def main():
  print("Maximum CPU load at any time: " + 
             str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + 
             str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + 
             str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()