# Problem:
# Given the head of a singly LinkedList, write a method to return the middle node of the LinkedList. If the total number
# of nodes in the LinkedList is even, return the second middle node.

# Solution:
# The brute force strategy would be to count the number of nodes in the LinkedList, and then find the middle node in the
# second iteration. But we can do this with one iteration using the fast and slow pointer method. We can make the fast
# pointer move twice as fast as the slow pointer, so by the time the fast pointer reaches the end of the LinkedList the
# slow pointer will be in the middle node.

# Time Complexity: O(N)
# The time complexity will be O(N), where N is the number of nodes in the LinkedList

# Space Complexity: O(1)
# The algorithm runs in constant space

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_middle_of_linked_list(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()