"""
Given a binary tree, return the sum of all left leaves 
of the tree. Ex: Given the following tree…

    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)

Ex: Given the following tree…

       2
      / \
    4    2
   / \ 
  3   9 
return 3
"""

from typing import Optional


class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None


def sumLeftLeaves(root: Optional[TreeNode]) -> int:
  # Time: O(n)
  # Space: O(n)
  if not root: return 0

  leftLeavesSum = 0

  stack = [root]

  while len(stack) != 0:
    currNode = stack.pop()

    if currNode.left:
      if not currNode.left.left and not currNode.left.right:
        leftLeavesSum += currNode.left.data
      stack.append(currNode.left)
    
    if currNode.right:
      stack.append(currNode.right)

  return leftLeavesSum


root_1 = TreeNode(5)
root_1.left = TreeNode(2)
root_1.right = TreeNode(12)
root_1.right.left = TreeNode(3)
root_1.right.right = TreeNode(8)

assert sumLeftLeaves(root_1) == 5


root_2 = TreeNode(2)
root_2.left = TreeNode(4)
root_2.right = TreeNode(2)
root_2.left.left = TreeNode(3)
root_2.left.right = TreeNode(9)

assert sumLeftLeaves(root_2) == 3


print("Passed all tests!")
