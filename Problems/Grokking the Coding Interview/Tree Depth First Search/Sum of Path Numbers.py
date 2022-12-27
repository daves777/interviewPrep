# Problem:
# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the
# total sum of all the numbers represented by all paths.

# Solution:
# As we are trying to search for a root-to-leaf path, we can follow the same DFS approach. We will need to keep track of the number
# representing the current path. This will entail multiplying 10 to the nodes as we go down the tree.

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# We will need O(N) space for the recursion stack

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  return find_root_to_leaf_path_numbers(root, 0)

def find_root_to_leaf_path_numbers(currentNode, pathSum):
  if currentNode is None:
    return 0

  # calculate the path number of the current node
  pathSum = currentNode.val + pathSum * 10

  # if the current node is a leaf, return the current path sum
  if currentNode.left is None and currentNode.right is None:
    return pathSum
  
  # traverse the left and the right subtree
  return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()