"""
Given a binary tree, return its zig-zag level order traversal 
(i.e. its level order traversal from left to right the first 
level, right to left the level the second, etc.).

Ex: Given the following tree…

    1
   / \
  2   3
return [[1], [3, 2]]


Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]

"""

from typing import Optional, List
from collections import deque


class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def zigzag(root: Optional[TreeNode]) -> List[List[int]]:
  # Time: O(n)
  # Space: O(n)
  startFromLeft = True

  output = []
  currLevel = deque()
  currLevel.append(root)

  while len(currLevel) != 0:
    nextLevel = deque()
    nodesValue = list()
    while len(currLevel) != 0:
      currNode = currLevel.popleft()
      
      nodesValue.append(currNode.data)

      if currNode.left: nextLevel.append(currNode.left)
      if currNode.right: nextLevel.append(currNode.right)

    currLevel = nextLevel
    if not startFromLeft:
      nodesValue.reverse()
    output.append(nodesValue)
    startFromLeft = not startFromLeft

  return output



bt_1 = TreeNode(1)
bt_1.left = TreeNode(2)
bt_1.right = TreeNode(3)

assert zigzag(bt_1) == [[1], [3, 2]]


bt_2 = TreeNode(8)
bt_2.left = TreeNode(2)
bt_2.right = TreeNode(29)
bt_2.right.left = TreeNode(3)
bt_2.right.right = TreeNode(9)

assert zigzag(bt_2) == [[8], [29, 2], [3, 9]]

print("Passed all tests!")