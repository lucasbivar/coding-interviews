"""
Given a binary tree, return whether or not it forms a reflection across
its center (i.e. a line drawn straight down starting from the root).
Note: a reflection is when an image, flipped across a specified line, forms the same image.

Ex: Given the following tree…

   2
 /   \
1     1
return true as when the tree is reflected across its center all the nodes match.

Ex: Given the following tree…

    1
   / \
  5   5
   \    \
    7    7
return false as when the tree is reflected across its center the nodes containing sevens do not match.
"""

from typing import Optional


class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None

def helper(node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
  if not node_1 and not node_2: return True
  if not node_1 or not node_2: return False
  if node_1.data != node_2.data: return False

  return helper(node_1.left, node_2.right) and helper(node_1.right, node_2.left)


def symmetricalTree(root: Optional[TreeNode]) -> bool:
  # Time: O(n)
  # Space: O(n)
  if not root: return True

  return helper(root.left, root.right)


root_1 = TreeNode(2)
root_1.left = TreeNode(1)
root_1.right = TreeNode(1)

assert symmetricalTree(root_1) == True


root_2 = TreeNode(1)
root_2.left = TreeNode(5)
root_2.left.right = TreeNode(7)
root_2.right = TreeNode(5)
root_2.right.right = TreeNode(7)

assert symmetricalTree(root_2) == False


print("Passed all tests!")