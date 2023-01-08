# Problem:
# Given a binary tree and a number 'S', find the number of paths in the tree such that the sum of all the node values of each
# path equals 'S'. The paths can start or end at any node but all paths must follow direction from parent to child (top to bottom)

# Solution:
# As we are trying to search for a root-to-leaf path, we can follow the same DFS approach. But we will need to four things:
# 1. Keep track of the current path in a list which will be passed to every recursive call
# 2. Whenever we traverse a node we will do two things:
#        a. Add current node to the current path
#        b. Find the sums of all sub-paths ending at the current node. If sum of any sub-path is equal to 'S', increment path count
# 3. Traverse all paths instead of stopping processing after finding the first path
# 4. Remove current node from the current path before returning from the function. This is needed to backtrack while going up the
#    recursive call stack to process other paths

# Time Complexity: O(N^2)
# The time complexity of this algorithm will be O(N) where N is the total number of nodes in the tree. This is because we traverse
# each node only once, but each time we traverse a node we go up the path to calculate the sums. The current path, in the worst case,
# can be O(N) in the case of a skewed tree. But, if the tree is balanced, then the current path will be equal to the height of the
# tree, i.e. O(logN). So the best case of our algorithm will be O(NlogN).

# Space Complexity: O(N)
# We will need O(N) space for the recursion stack. We will also need O(N) space for storing currentPath in the worst case.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  return count_paths_recursive(root, S, [])

def count_paths_recursive(currentNode, S, currentPath):
  if currentNode is None:
    return 0
  
  currentPath.append(currentNode.val) # add current node value to path
  pathCount, pathSum = 0, 0
  for i in range(len(currentPath) - 1, -1, -1): # find sums of all sub-paths in current path list going upwards
    pathSum += currentPath[i]
    if pathSum == S: # if any sub-path is equal to 'S', increment path count
      pathCount += 1
  
  pathCount += count_paths_recursive(currentNode.left, S, currentPath) # traverse left sub tree
  pathCount += count_paths_recursive(currentNode.right, S, currentPath) # traverse right sub tree

  del currentPath[-1] # remove node from the path to backtrack as we go up the recursive call stack

  return pathCount


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()