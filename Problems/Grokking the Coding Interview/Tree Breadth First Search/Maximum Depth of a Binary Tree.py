# Problem:
# Given a binary tree, find its maximum depth(or height).

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern, and is very similar to Minimum Depth of a
# Binary Tree. In this case, instead of returning as soon as we find a leaf node, we will keep traversing for all
# the levels, incrementing the depth each time we complete a level.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we are returning a list containing the averages. We will also need O(N) space for the
# queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will
# need O(N) space to store them in the queue.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_maximum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root) # add root node to queue
  treeDepth = 0
  while queue:
    levelSize = len(queue) # determine size of level
    treeDepth += 1 # increment tree depth
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child
  return treeDepth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()