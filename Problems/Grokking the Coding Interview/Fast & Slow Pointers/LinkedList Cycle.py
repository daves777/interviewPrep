# Problem:
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

# Solution:
# We can solve this using a fast and slow pointer. If the LinkedList doesn't have a cycle in it, the fast pointer will
# reach the end of the LinkedList before the slow pointer and reveal there is no cycle. If the LinkedList does have a
# cycle, the fast pointer will enter the cycle first, followed by the slow pointer. If at any stage both of these
# pointers meet, we can conclude that the LinkedList has a cycle in it.

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def has_cycle(head):
  slow, fast, = head, head # set both slow and fast to head
  while fast is not None and fast.next is not None: # while fast exists, and one ahead of fast also exists
    fast = fast.next.next # fast pointer moves two
    slow = slow.next # slow pointer moves one
    if slow == fast: # if slow is same as fast node
      return True # found a cycle
  return False # if there is no cycle, fast will reach end of linkedlist first

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

main()

# Problem:
# Given the head of a LinkedList with a cycle, find the length of the cycle

# Solution: We can use a similar solution to find the cycle length. Once we determine that the LinkedList contains a cycle, we
# can save the slow pointer and iterate the whole cycle with another pointer until we see the same poinnter again to find the
# length of the cycle.

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      return calculate_cycle_length(slow)
  return 0

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
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()