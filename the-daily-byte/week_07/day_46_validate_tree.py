"""
Given a binary tree, containing unique values, determine if it is 
a valid binary search tree.
Note: the invariants of a binary search tree (in our case) are all
values to the left of a given node are less than the current node’s 
value, all values to the right of a given node are greater than the 
current node’s value, and both the left and right subtrees of a given 
node must also be binary search trees.

Ex: Given the following binary tree…

   1
 /   \
2     3
return false.
Ex: Given the following tree…

   2
 /   \
1     3
return true.
"""

from typing import Optional
import math

class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None


def validateTree(root: Optional[TreeNode], lessThan=math.inf, greaterThan=-math.inf) -> bool:
  # Time: O(n)
  # Space: O(n)
  if not root: 
    return True
  
  if root.data >= lessThan or root.data <= greaterThan: 
    return False
  
  return validateTree(root.left, root.data, greaterThan) and validateTree(root.right, lessThan, root.data)


root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.right = TreeNode(3)

assert validateTree(root_1) == False


root_2 = TreeNode(2)
root_2.left = TreeNode(1)
root_2.right = TreeNode(3)

assert validateTree(root_2) == True


print("Passed all tests!")