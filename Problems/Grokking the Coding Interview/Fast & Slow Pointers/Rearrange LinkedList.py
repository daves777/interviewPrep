# Problem:
# Given the head of a singly LinkedList, write a method to modify the LinnkedList such that the nodes from the second half
# of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the Linkedlist has
# nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, the method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null

# The algorithm must use constant space, and the input list should be modified in place.

# Solution:
# This problem is similar to Palindrome Linkedlist. To rearrange the LinkedList we will follow these steps:

# Steps:
# 1. Use Fast & Slow pointers similar to Middle of LinkedList to find the middle node of the LinkedList
# 2. Once we have the middle of the LinkedList, reverse the second half of the LinkedList
# 3. Finally, we'll iterate through the first half and the reversed second half to produce a LinkedList in the required order

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
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  if head is None or head.next is None:
    return

  # find the middle of LinkedList
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  
  # slow is now pointing to middle node
  head_second_half = reverse(slow) # reverse second half
  head_first_half = head

  # rearrange to produced LinkedList in required order
  while head_first_half is not None and head_second_half is not None:
    temp = head_first_half.next # save first half next head
    head_first_half.next = head_second_half # set first half head next to head of second half
    head_first_half = temp # set first half head to temp we saved earlier

    temp = head_second_half.next # save second half next head
    head_second_half.next = head_first_half # set second half head next to current head of first half
    head_second_half = temp # set second half head to temp we saved earlier
  
  # set the next of the last node to 'None'
  if head_first_half is not None:
    head_first_half.next = None

def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
