"""
Given a binary tree, return its maximum depth.
Note: the maximum depth is defined as the number of nodes along 
the longest path from root node to leaf node.

Ex: Given the following tree…

    9
   / \
  1   2
return 2


Ex: Given the following tree…

    5
   / \
  1  29
    /  \
   4   13
return 3
"""

from typing import Optional


class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None


def calculateDepth(root: Optional[TreeNode]) -> int:
  # Time: O(n)
  # Space: O(m) -> max depth
  if not root: return 0

  depth_1 = 1 + calculateDepth(root.left)

  depth_2 = 1 + calculateDepth(root.right)

  return max(depth_1, depth_2)


root_1 = TreeNode(9)
root_1.left = TreeNode(1)
root_1.right = TreeNode(2)

assert calculateDepth(root_1) == 2


root_2 = TreeNode(5)
root_2.left = TreeNode(1)
root_2.right = TreeNode(29)
root_2.right.left = TreeNode(4)
root_2.right.right = TreeNode(13)

assert calculateDepth(root_2) == 3


print("Passed all tests!")