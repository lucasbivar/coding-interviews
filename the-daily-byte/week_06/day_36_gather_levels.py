"""
Given a binary tree, return its level order traversal where the nodes 
in each level are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]


Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]


Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
"""

from typing import List, Optional
from collections import deque

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def gatherLevels(root: Optional[TreeNode]) -> List[List[int]]:
  # Time: O(n)
  # Space: O(n)
  if not root: return []

  output = []
  currLevel = deque()
  currLevel.append(root)

  while len(currLevel) != 0:
    nodesValues = []
    nextLevel = deque()

    while len(currLevel) != 0:
      currNode = currLevel.popleft()
      nodesValues.append(currNode.data)

      if currNode.left:
        nextLevel.append(currNode.left)
      if currNode.right:
        nextLevel.append(currNode.right)
    
    currLevel = nextLevel
    output.append(nodesValues)
  
  return output



bt_1 = TreeNode(4)
bt_1.left = TreeNode(2)
bt_1.right = TreeNode(7)

assert gatherLevels(bt_1) == [[4], [2, 7]]


bt_2 = TreeNode(2)
bt_2.left = TreeNode(10)
bt_2.right = TreeNode(15)
bt_2.right.right = TreeNode(20)

assert gatherLevels(bt_2) == [[2], [10, 15], [20]]


bt_3 = TreeNode(1)
bt_3.left = TreeNode(9)
bt_3.left.left = TreeNode(3)
bt_3.right = TreeNode(32)
bt_3.right.right = TreeNode(78)

assert gatherLevels(bt_3) == [[1], [9, 32], [3, 78]]


bt_4 = TreeNode(1)
bt_4.left = TreeNode(9)
bt_4.left.left = TreeNode(3)
bt_4.left.right = TreeNode(2)
bt_4.right = TreeNode(32)
bt_4.right.left = TreeNode(40)
bt_4.right.right = TreeNode(78)

assert gatherLevels(bt_4) == [[1], [9, 32], [3, 2, 40, 78]]

print("Passed all tests!")