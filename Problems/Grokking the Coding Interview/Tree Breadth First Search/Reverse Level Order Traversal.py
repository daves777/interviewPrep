# Problem:
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level
# comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, except instead of appending
# the current level at the end, we'll append the current level at the beginning of the result list.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we are returning a list containing the level order traversal. We also need O(N) space for
# the queue.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = deque()
  if root is None:
    return result
  
  queue = deque()
  queue.append(root) # add root node to queue

  while queue:
    levelSize = len(queue) # determine size of level
    currentLevel = [] # create empty array for current level
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      currentLevel.append(currentNode.val) # add currentNode value to array for current level
      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child
    result.appendleft(currentLevel) # add level to result array
  
  return result



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()