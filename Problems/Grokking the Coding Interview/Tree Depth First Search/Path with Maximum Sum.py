# Problem:
# Find the path with the maxiumum sum in a given binary tree. Write a function that returns the maximum sum. A path can be
# defined as a sequence of nodes between any two nodes and doesn't necessarily pass through the root. The path must contain
# at least one node.

# Solution:
# This problem follows the Binary Tree Path Sum pattern, and we can use a DFS approach. We can use a similar approach to
# Tree Diameter. The difference would be to ignore paths with negative sums.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once.

# Space Complexity: O(N)
# We will need O(N) space for the recursion stack.

import math

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_maximum_path_sum(root):
  maxSum = -math.inf # set to negative infinity in case max sum is negative

  def maxPathSumRecursive(currentNode):
    if currentNode is None:
      return 0

    nonlocal maxSum # establish that variable diameter does not belong to inner function

    leftPathSum = maxPathSumRecursive(currentNode.left) # traverse left sub tree
    rightPathSum = maxPathSumRecursive(currentNode.right) # traverse right sub tree

    # we need to find the maximum sum so we should ignore any path that has an overall negative sum
    leftPathSum = max(leftPathSum, 0)
    rightPathSum = max(rightPathSum, 0)

    # current sum is equal to left path sum + right path sum + value of current node
    currentSum = leftPathSum + rightPathSum + currentNode.val
    maxSum = max(maxSum, currentSum) # update global max sum

    # max sum of any path is equal to max of left and right path sum plus value of current node
    return max(leftPathSum, rightPathSum) + currentNode.val
  
  maxPathSumRecursive(root)
  return maxSum

def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()