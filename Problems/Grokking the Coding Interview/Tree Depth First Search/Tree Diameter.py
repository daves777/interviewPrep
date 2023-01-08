# Problem:
# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between
# any two leaf nodes. The diameter of a tree may or may not pass through the root. You can always assume that there are at least
# two leaf nodes in the given tree.

# Solution:
# This problem follows the Binary Tree Path Sum pattern, and we can use a DFS approach. We will need to do the following:
# 1. At every step, find the height of both children of the current node. To do this, we will make to recursive calls
# 2. The height of current node is equal to the max of the heights of its left and right children, plus 1 for the current node
# 3. The tree diameter at the current node is equal to the height of the left and right child plus 1 for the current node
# 4. We will keep track of the max diameter with a variable, and update it whenever we find a larger diameter.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once.

# Space Complexity: O(N)
# We will need O(N) space for the recursion stack.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def tree_diameter(root):
  diameter = 0

  def longest_path(currentNode):
    if currentNode is None:
      return 0

    nonlocal diameter # establish that variable diameter does not belong to inner function

    left_path = longest_path(currentNode.left) # traverse left sub tree
    right_path = longest_path(currentNode.right) # traverse right sub tree

    # if the current node has a left and right sub tree, we can calculate the diameter at current node
    if left_path != 0 and right_path != 0:
      
      # diameter at current node will be height of left sub tree + height of right subtree + 1 for current node
      currentDiameter = left_path + right_path + 1
      diameter = max(diameter, currentDiameter) # update global tree diameter

    # height of current node will be equal to max of left and right sub tree plus 1 for current node
    return max(left_path, right_path) + 1
  
  longest_path(root)
  return diameter

def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(tree_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(tree_diameter(root)))


main()
print()

# Alternate problem: Find the length of the largest diameter where the length is determined by the number of edges

def tree_diameter(root):
  treeDiameter = 0

  def longest_path(currentNode):
    if currentNode is None:
      return 0
    
    nonlocal treeDiameter # establish that variable diameter does not belong to inner function

    left_path = longest_path(currentNode.left) # traverse left sub tree
    right_path = longest_path(currentNode.right) # traverse right sub tree

    treeDiameter = max(treeDiameter, left_path + right_path) # update diameter if current diameter is larger

    return max(left_path, right_path) + 1 # return longest path between left and right plus 1 for path between node and parent
  
  longest_path(root)
  return treeDiameter

main()