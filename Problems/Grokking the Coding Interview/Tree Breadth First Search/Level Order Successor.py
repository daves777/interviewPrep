# Problem:
# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the
# node that appears right after the given node in the level order traversal.

# Solution:
# This problem follows the Binary Tree Level Order Traversal pattern. We can use the same BFS approach, except we wonn't keep
# track of all the levels. Instead, we'll keep inserting child nodes to the queue. As soon as we find the given node, we'll
# return the nenxt node from the queue as the level order successor.

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


def find_successor(root, key):
  if root is None:
    return None
  
  queue = deque()
  queue.append(root) # add root node to queue

  while(queue):
    currentNode = queue.popleft() # set currentNode to first in queue
    if currentNode.val == key: # break if we found the key
      break
    if currentNode.left:
      queue.append(currentNode.left) # add left child
    if currentNode.right:
      queue.append(currentNode.right) # add right child

  return queue[0] if queue else None

def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()