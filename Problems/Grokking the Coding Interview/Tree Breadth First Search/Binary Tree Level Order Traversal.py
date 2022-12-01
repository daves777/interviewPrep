# Problem:
# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all
# nodes of each level from left to right in separate sub-arrays.

# Solution:
# Since we need to traverse all nodes of each level before moving onto the next level, we can use Breadth First Search(BFS)
# to solve this problem. We can use a Queue to traverse in BFS fashion.

# Steps:
# 1. Start by pushing root node to the queue
# 2. Keep iterating until the queue is empty
# 3. Each iteration, count the elements in the queue(let's call it levelSize). We will have these many nodes in the current level
# 4. Remove levelSize nodes from the queue and push their value in an array to represent the current value
# 5. After removinng each node from the queue, insert both children into the queue
# 6. If the queue is not empty, repeat from step 3 for the next level

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
  result = []
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
    result.append(currentLevel) # add level to result array
  
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()