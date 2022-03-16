"""
Given a binary tree, return the largest value in each of its levels. 

Ex: Given the following tree…

    2
   / \
  10  15
        \
         20
return [2, 15, 20]


Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
"""

from typing import Deque, Optional, List
from collections import deque
from math import inf

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def maxValueInEachLevel(head: Optional[TreeNode]) -> List[int]:
  # Time: O(n)
  # Space: O(n)
  if not head: return []

  output: List[int] = []

  currLevel: Deque[TreeNode] = deque()
  currLevel.append(head)

  while len(currLevel) != 0:
    nextLevel: Deque[TreeNode] = deque()
    maxValue = -inf

    while len(currLevel) != 0:
      currNode: TreeNode = currLevel.popleft()
      maxValue = max(maxValue, currNode.data)

      if currNode.left:
        nextLevel.append(currNode.left)

      if currNode.right:
        nextLevel.append(currNode.right)
    
    output.append(maxValue)
    currLevel = nextLevel
  
  return output

bt_1 = TreeNode(2)
bt_1.left = TreeNode(10)
bt_1.right = TreeNode(15)
bt_1.right.right = TreeNode(20)

assert maxValueInEachLevel(bt_1) == [2, 15, 20]


bt_2 = TreeNode(1)
bt_2.left = TreeNode(5)
bt_2.right = TreeNode(6)
bt_2.left.left = TreeNode(5)
bt_2.left.right = TreeNode(3)
bt_2.right.right = TreeNode(7)

assert maxValueInEachLevel(bt_2) == [1, 6, 7]

print("Passed all tests!")