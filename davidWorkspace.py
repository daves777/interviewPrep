# Problem:
# Given the head of a singly LinkedList, write a method to check if the LinkedList is a palindrome or not. A palindrome
# LinkedList will have node values that read the same backward or forward.

# The algorithm must use constant space, and the input list should be in the original form once the algorithm is finished.
# The algorithm must have O(N) run time where 'N' is the number of nodes in the LinkedList

# Solution:
# If we divide the LinkedList into two halves, the node values in the first half in the forward direction should be similar to 
# the node values of the second half in nthe backward direction. Since this is a singly linked list, we can't move backwards.
# We can handle this with the following steps:

# Steps:
# 1. We can use fast and slow pointers to determine to find the middle node of the LinkedList
# 2. Once we have the middle of the LinkedList, we can reverse the second half
# 3. We can compare the first half with the reversed second half to see if they are the same
# 4. We will reverse the second half of the LinkedList to revert it back to the original form

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True
  
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  
  middle_pointer = reverse(slow)
  middle_pointer_copy = middle_pointer

  while head is not None and middle_pointer is not None:
    if head.value != middle_pointer.value:
      break
    head = head.next
    middle_pointer = middle_pointer.next
  
  reverse(middle_pointer_copy)

  if head is None or middle_pointer is None:
    return True
  
  return False

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
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()