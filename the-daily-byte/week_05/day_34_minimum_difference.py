"""
Given a binary search tree, return the minimum difference 
between any two nodes in the tree.


Ex: Given the following tree...
        2
       / \
      3   1
return 1.


Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.


Ex: Given the following tree...
        2
         \
         100
return 98.
"""

from typing import List, Optional
from math import inf

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def inorderTraversal(root: Optional[TreeNode], inorderArr: List[int]) -> None:
  if not root: return

  inorderTraversal(root.left, inorderArr)

  inorderArr.append(root.data)

  inorderTraversal(root.right, inorderArr)


def minimumDifference(root: Optional[TreeNode]) -> int:
  # Time: O(n)
  # Space: O(n)

  inorderArr: List[int] = []
  inorderTraversal(root, inorderArr)
  if len(inorderArr) < 2: return -1

  minDiff: int = inf
  for i in range(1, len(inorderArr)):
    minDiff = min(minDiff, abs(inorderArr[i]-inorderArr[i-1]))

  return minDiff


bst_1 = TreeNode(2)
bst_1.left = TreeNode(3)
bst_1.right = TreeNode(1)

assert minimumDifference(bst_1) == 1


bst_2 = TreeNode(29)
bst_2.left = TreeNode(17)
bst_2.left.left = TreeNode(1)
bst_2.right = TreeNode(50)
bst_2.right.left = TreeNode(42)
bst_2.right.right = TreeNode(59)

assert minimumDifference(bst_2) == 8


bst_3 = TreeNode(2)
bst_3.right = TreeNode(100)

assert minimumDifference(bst_3) == 98

print("Passed all tests!") 