# Problem:
# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the
# root node to the nearest leaf node.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, except instead of
# keeping track of all nodes of a level, we will keep track of the depth of the tree. As soon as we find our first leaf
# node, that level will represent the minimum depth of the tree.

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


def find_minimum_depth(root):
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

      if not currentNode.left and not currentNode.right: # check if currentNode is leaf node
        return treeDepth # return first occurence of leaf node

      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()