# Problem:
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed
# LinkedList.

# Solution:
# To reverse a LinkedList, we need to reverse one node at a time. We start with a variable current which will point to the head
# of the LinnkedList and a variable previous which will point to the previous node that we have processed. Initially, previous
# will be null. Step by step, we will reverse the current node by pointing to the previous node before moving on to the next
# nnode. Also, we will always update previous to point to the previous node that we processed.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the LinkedList

# Space Complexity: O(1)
# We only used constant space, so the space complexity will be O(1)

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  current, prev = head, None
  while current is not None:
    next = current.next # temporarily store the next node
    current.next = prev # reverse the current node by pointing it towards previous
    prev = current # before moving to next node, point previous to current node
    current = next # move on to next node
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()