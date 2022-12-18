# Problem:
# Given a binary tree and a number S, find all paths from root-to-leaf such that the sum of all node values of each path equals S

# Solution:
# As we are trying to search for a root-to-leaf path, we can follow the same DFS approach. The difference is that instead of stopping
# as soon as we find the first path, every time we find a root-to-leaf path we will store it in a list. 

# Time Complexity: O(N^2)
# The time complexity of this algorithm will be O(N^2) where N is the total number of nodes in the tree. This is because we traverse
# each node once, and for every leaf node we might have to store its path by making a copy of the current path, which takes O(N)

# Space Complexity: O(N)
# If we ignore the space needed for the allPaths list, we will need O(N) space for the recursion stack.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, required_sum):
  allPaths = []
  find_paths_recursive(root, required_sum, [], allPaths)
  return allPaths

def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
  if currentNode is None:
    return
  
  currentPath.append(currentNode.val)

  if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  else:
    find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
    find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)
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