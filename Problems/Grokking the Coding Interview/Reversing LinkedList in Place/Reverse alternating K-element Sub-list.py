# Problem:
# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head. If,
# in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# Solution:
# This is similar to Reverse every K-element Sub-list. THe difference is that we have to skip 'k' alternating elements. We
# can follow the same approach except each time we reverse 'k' elements, we'll skip the next 'k' elements.

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


def reverse_every_k_elements(head, k):
  if head is None or k < 1:
    return head
  
  current, previous = head, None
  while current is not None:
    previous_part_last_node = previous # remember last node of previous part
    sub_list_last_node = current # after reversing the sublist, current will become the last node in the sublist
    i = 0
    while current is not None and i < k: # reverse k nodes
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1
    
    if previous_part_last_node is not None:
      previous_part_last_node.next = previous # connect with previous part
    else:
      head = previous # if previous_part_last_node is None, that means we are on the first sublist, so the head becomes previous
    
    # connect with next part
    sub_list_last_node.next = current

    i = 0
    while current is not None and i < k: # skip k nodes
      previous = current
      current = current.next
      i += 1
  
  return head
    

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()