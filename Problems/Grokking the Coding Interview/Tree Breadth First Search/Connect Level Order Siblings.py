# Problem:
# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, but we'll have to 
# remember the previous node to connect it with the current node

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we will need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any
# level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None
  
  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

def connect_level_order_siblings(root):
  if root is None:
    return
  
  queue = deque()
  queue.append(root) # add root node to queue
  while queue:
    previousNode = None
    levelSize = len(queue) # determine size of level
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      if previousNode: # if previous node is valid
        previousNode.next = currentNode # connect previous node to current node
      previousNode = currentNode
      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()