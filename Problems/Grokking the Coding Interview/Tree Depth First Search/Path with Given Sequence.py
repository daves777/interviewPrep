# Problem:
# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

# Solution:
# As we are trying to search for a root-to-leaf path, we can follow the same DFS approach. We will need to track the element of the
# given sequence that we should match with the current node. We can return false as soon as we find a mismatch between the sequence
# and the node value.

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


def find_path(root, sequence):
  if not root:
    return len(sequence) == 0
  return find_path_recursive(root, sequence, 0)

def find_path_recursive(currentNode, sequence, sequenceIndex):
  if currentNode is None:
    return False

  # If currentNode doesn't match sequence values or current path is longer than sequence
  if currentNode.val != sequence[sequenceIndex] or sequenceIndex >= len(sequence):
    return False
  
  # If current node is leaf node and it is end of sequence, we have found the path
  if currentNode.left is None and currentNode.right is None and sequenceIndex == len(sequence) - 1:
    return True
  else:
    # Recursively call to traverse the left and right subtree, return true if either of them return true
    return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()