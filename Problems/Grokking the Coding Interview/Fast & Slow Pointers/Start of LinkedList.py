# Problem:
# Given the head of a Singly LinkedList, write a function to find the starting node of the cycle

# Solution:
# If we know the length of the LinkedList cycle, we can find the start of the cycle by moving one pointer 'k' nodes
# ahead. Since the pointer will be ahead of the first pointer by the length of nodes, it must have completed one
# loop in the cycle by the time both pointers meet.

# Steps:
# 1. Set two pointers to the start of the LinkedList. We'll call them pointer1 and pointer 2
# 2. Find the length of the LinkedList cycle using approach from LinkedList Cycle
# 3. Assuming the length of the cycle is K, Move pointer2 ahead by K nodes
# 4. Keep incrementing pointer1 and pointer2 until they meet to find the cycle starting point

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  # first, find the cycle
  slow, fast = head, head
  cycle_length = 0
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      cycle_length = calculate_cycle_length(slow) # then, find the cycle length
      break
  # now, using cycle length find the start
  pointer1, pointer2 = head, head
  # move pointer2 ahead by cycle_length nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1

def calculate_cycle_length(slow):
  current = slow
  length = 0
  while True:
    current = current.next
    length += 1
    if current == slow:
      break
  return length

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()