# Problem:
# Given a binary tree, populate an array to represent the averages of all of its levels.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, except instead of
# keeping track of all nodes of a level, we will only need to keep track of the runnning sum of the values in each level.
# Then, we will append the average of the current level to the result array

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

def find_level_averages(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root) # add root node to queue

  while queue:
    levelSize = len(queue) # determine size of level
    levelSum = 0.0 # create empty array for current level
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      levelSum += currentNode.val # add currentNode value to running sum for current level
      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child
    result.append(levelSum/levelSize) # add current level average innto result array
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()