"""
Given a binary tree and a target, return whether or 
not there exists a root to leaf path such that all 
values along the path sum to the target.

Ex: Given the following tree…

      1
     / \
    5   2
   /   / \
  1  12   29
and a target of 15, return true as the path 1->2->12 sums to 15.

Ex: Given the following tree…

     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
"""

from typing import Optional

class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None


def helper(root: Optional[TreeNode], target: int, currSum: int) -> bool:
  if not root: return False
  
  currSum += root.data

  if not root.left and not root.right:
    return currSum == target
  
  return helper(root.left, target, currSum) or helper(root.right, target, currSum)

def rootToLeafPathSum(root: Optional[TreeNode], target: int) -> bool:
  # Time: O(n)
  # Space: O(n)
  return helper(root, target, 0)


root_1 = TreeNode(1)
root_1.left = TreeNode(5)
root_1.left.left = TreeNode(1)
root_1.right = TreeNode(2)
root_1.right.left = TreeNode(12)
root_1.right.right = TreeNode(29)

assert rootToLeafPathSum(root_1, 15) == True


root_2 = TreeNode(104)
root_2.left = TreeNode(39)
root_2.left.left = TreeNode(32)
root_2.left.right = TreeNode(31)
root_2.right = TreeNode(31)
root_2.right.left = TreeNode(9)
root_2.right.right = TreeNode(10)

assert rootToLeafPathSum(root_2, 175) == True

print("Passed all tests!")