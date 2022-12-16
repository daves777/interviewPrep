# Problem:
# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of
# nodes visible when the tree is seen from the right side.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, but we'll add the
# last node of each level.

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
    self.left, self.right = None, None


def tree_right_view(root):
  if root is None:
    return
  
  result = []
  queue = deque()
  queue.append(root) # add root node to queue
  while queue:
    levelSize = len(queue) # determine size of level
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      if (i == levelSize - 1): # if this is the last node of the level, add to result array
        result.append(currentNode)
      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()