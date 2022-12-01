# Problem:
# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all
# nodes of the first level from left to right, thenn right to left for the next level and keep alternatinng in the same manner
# for the following levels.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, except we'll have to
# remember to alternate the level order traversal. This means for every other level, we will traverse similar to Reverse
# Level Order Traversal. We'll use a dequeue object instead of an array for currentLevel and switch between adding from the
# left and right.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we are returning a list containing the zig zag traversal. We also need O(N) space for
# the queue.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result
  
  leftToRight = True
  queue = deque()
  queue.append(root) # add root node to queue
  while queue:
    levelSize = len(queue) # determine size of level
    currentLevel = deque() # create queue object for current level so we can add to left and right
    for i in range(levelSize):
      currentNode = queue.popleft() # set currentNode to first in queue
      
      # add currentNode value to current level based on traverse direction
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)

      if currentNode.left:
        queue.append(currentNode.left) # add left child
      if currentNode.right:
        queue.append(currentNode.right) # add right child
        
    result.append(list(currentLevel)) # add level to result array

    leftToRight = not leftToRight # reverse traversal direction

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()