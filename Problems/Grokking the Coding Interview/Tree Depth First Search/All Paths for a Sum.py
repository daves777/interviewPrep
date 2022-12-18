# Problem:
# Given a binary tree and a number S, find all paths from root-to-leaf such that the sum of all node values of each path equals S

# Solution:
# As we are trying to search for a root-to-leaf path, we can follow the same DFS approach. The difference is that instead of stopping
# as soon as we find the first path, every time we find a root-to-leaf path we will store it in a list. 

# Time Complexity: O(N)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once

# Space Complexity: O(N)
# Thee space required will be O(N) because we will need O(N) space for the recursion stack.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, required_sum):
  allPaths = []
  find_paths_recursive(root, required_sum, [], allPaths) # invoke recursive function
  return allPaths

def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
  if currentNode is None:
    return

  currentPath.append(currentNode.val) # add current node to the path
  
  # if current node is a leaf node and value is equal to required_sum, add current path to final list
  if currentNode.left is None and currentNode.right is None and currentNode.val == required_sum:
    allPaths.append(list(currentPath))
  else:
    # traverse left sub tree
    find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
    # traverse right sub tree
    find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)
  # remove current node from the path to backtrack
  # we need to remove the current node while going up the recursive call stack
  del currentPath[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()