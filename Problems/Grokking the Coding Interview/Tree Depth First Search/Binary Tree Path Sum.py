# Problem:
# Given a binary tree and a number S, find if the tree has a path from root-to-leaf such that the sum of all the node values
# of that path equals S.

# Solution:
# As we are trying to search for a root-to-leaf path, we can use Depth First Search to solve this problem. To recursively traverse
# a binary tree in a DFS fashion, we can start from the root and at every step, maake two recursive calls one for the left and one
# for the right child

# Steps:
# 1. Start DFS with the root of the tree
# 2. If the current node is not a leaf node, do two things:
#       a. Subtract the value of the current node from the given number to get a new sum S = S - node.val
#       b. Make two recursive calls for both the children of the current node with the new number calculated in the previous step
# 3. Every step, see if current node is a leaf node and if its value is equal to S. If both are true, return true as we've found the path
# 4. If the current node is a leaf but its value is not equal to the given number S, return false

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we will need O(N) space for the recursion stack.

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right
  
def has_path(root, sum):
  if root is None: # if root node is null, return false
    return False
  
  if root.left is None and root.right is None and root.val == sum: # if current node is leaf node and value is equal to sum return
    return True
  
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val) # recursively call to traverse left and right child

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()