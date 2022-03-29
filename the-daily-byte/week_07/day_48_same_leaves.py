"""
Given two binary trees, return whether or not both trees have the same 
leaf sequence. Two trees have the same leaf sequence if both trees’ leaves 
read the same from left to right.

Ex: Given the following trees…

   1
 /   \
1     3
and


   7
 /   \
1     2
return false as both the trees' leaves don't read the same from left 
to right (i.e. [1, 3] and [1, 2]).

Ex: Given the following trees…

    8
   / \
  2   29
    /  \
   3    9

and

    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3

return true as both the trees' leaves read the same from left
to right (i.e. [2, 3, 9] and [2, 3, 9]).
"""

from typing import Optional, List


class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None
  

def leavesToList(root: Optional[TreeNode], arr: List[int]) -> None:
  if not root: return

  if not root.left and not root.right:
    arr.append(root.data)
  
  if root.left:
    leavesToList(root.left, arr)
  
  if root.right:
    leavesToList(root.right, arr)


def sameLeaves(root_1: Optional[TreeNode], root_2: Optional[TreeNode]) -> bool:
  # Time: O(n + m)
  # Space: O(n + m)

  leavesFromRoot_1 = list()
  leavesToList(root_1, leavesFromRoot_1)

  leavesFromRoot_2 = list()
  leavesToList(root_2, leavesFromRoot_2)

  if len(leavesFromRoot_1) != len(leavesFromRoot_2): 
    return False

  for i in range(len(leavesFromRoot_1)):
    if leavesFromRoot_1[i] != leavesFromRoot_2[i]:
      return False
  
  return True



root_1_1 = TreeNode(1)
root_1_1.left = TreeNode(1)
root_1_1.right = TreeNode(3)

root_1_2 = TreeNode(7)
root_1_2.left = TreeNode(1)
root_1_2.right = TreeNode(2)

assert sameLeaves(root_1_1, root_1_2) == False


root_2_1 = TreeNode(8)
root_2_1.left = TreeNode(2)
root_2_1.right = TreeNode(29)
root_2_1.right.left = TreeNode(3)
root_2_1.right.right = TreeNode(9)

root_2_2 = TreeNode(8)
root_2_2.left = TreeNode(2)
root_2_2.right = TreeNode(29)
root_2_2.left.left = TreeNode(2)
root_2_2.right.left = TreeNode(3)
root_2_2.right.right = TreeNode(9)
root_2_2.right.left.right = TreeNode(3)

assert sameLeaves(root_2_1, root_2_2) == True


print("Passed all tests!")

