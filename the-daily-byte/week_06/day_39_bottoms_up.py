"""
Given a binary tree, returns of all its levels in a bottom-up 
fashion (i.e. last level towards the root). 

Ex: Given the following tree…

        2
       / \
      1   2
return [[1, 2], [2]]


Ex: Given the following tree…

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
"""

from typing import Deque, Optional, List
from collections import deque

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def bottomsUp(root: Optional[TreeNode]) -> List[List[int]]:
  # Time: O(n)
  # Space: O(n)
  if not root: return []

  output: Deque[List[int]] = deque()

  currLevel: Deque[TreeNode] = deque()
  currLevel.append(root)


  while len(currLevel) != 0:
    nextLevel: Deque[TreeNode] = deque()
    currNodesValues: List[int] = []

    while len(currLevel) != 0:
      currNode: TreeNode = currLevel.popleft()
      currNodesValues.append(currNode.data)

      if currNode.left:
        nextLevel.append(currNode.left)

      if currNode.right:
        nextLevel.append(currNode.right)
    
    currLevel = nextLevel
    output.appendleft(currNodesValues)
  
  return list(output)


bt_1 = TreeNode(2)
bt_1.left = TreeNode(1)
bt_1.right = TreeNode(2)

assert bottomsUp(bt_1) == [[1, 2], [2]]


bt_2 = TreeNode(7)
bt_2.left = TreeNode(6)
bt_2.right = TreeNode(2)
bt_2.left.left = TreeNode(3)
bt_2.left.right = TreeNode(3)

assert bottomsUp(bt_2) == [[3, 3], [6, 2], [7]]


print("Passed all tests!")
