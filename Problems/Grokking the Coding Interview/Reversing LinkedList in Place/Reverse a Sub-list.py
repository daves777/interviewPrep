# Problem:
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

# Solution:
# We can use the same process within Reverse a LinkedList to solve this problem.

# Steps:
# 1. Skip the first p - 1 nodes to reach the node at position p
# 2. Remember the node at position p - 1 to be used later to connect with the reversed sub-list
# 3. Reverse the nodes from p to q using the same approach in Reverse a LinkedList
# 4. Connect the p - 1 and q + nodes to the reversed sub-list

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


def reverse_sub_list(head, p, q):
  if p == q:
    return head
  
  current, previous = head, None
  i = 0
  while current is not None and i < p - 1: # iterate until current points to pth node
    previous = current
    current = current.next
    i += 1
  
  first_half_last_node = previous # save the last node of the first half
  sub_list_last_node = current # after reversing the sublist, current will become the last node in the sublist

  i = 0
  while current is not None and i < q - p + 1: # reverse nodes between p and q
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1
  
  if first_half_last_node is not None:
    first_half_last_node.next = previous # connect to first half, previous is now the first node of the sublist
  else: # if first_half_last_node is None, it is because p == 1, so previous was never set.
    head = previous # change the head to previous
  
  # connect with last part
  sub_list_last_node.next = current
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()