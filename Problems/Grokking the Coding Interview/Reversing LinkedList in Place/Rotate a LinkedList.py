# Problem:
# Given the head of a Singly LinkedList and a number 'k', rotate the LinkedList to the right by 'k' nodes.

# Solution:
# We essentially need to take the sublist of 'k' ending nodes and put them in the beginning. That means we need to do three
# things. We need to connect the last node of the LinkedList to the head, because the list will have a different tail after
# the rotation. The new head of the LinkedList needs to be the node at the beginning of the sublist. And the node right before
# the start of the sublist will be the new tail of the rotated LinkedList

# Steps:
# 1. Find the length of the list and the last node in the list.
# 2. Connect the last node with the head to make a ciruclar list
# 3. Iterate through to set the head of the list to start of sublist
# 4. Set last node of rotated list to none

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


def rotate(head, rotations):
  if head is None or head.next is None or rotations == 0:
    return head
  
  # find the length and the last node of the list
  last_node = head
  length = 1 # initialize list length to 1
  while last_node.next is not None:
    last_node = last_node.next
    length += 1
  
  last_node.next = head # connect the last node with the head to make it a circular list
  rotations %= length # if rotations is larger than the length of the list, find the actual number to shift by
  skip_length = length - rotations # determine length of nodes to iterate to find head again
  rotated_list_last_node = head
  # iterate until rotated_list_last_node points to the node right before the sublist of k ending nodes
  for i in range(skip_length - 1):
    rotated_list_last_node = rotated_list_last_node.next

  # set head and tail of new LinkedList
  head = rotated_list_last_node.next
  rotated_list_last_node.next = None
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()