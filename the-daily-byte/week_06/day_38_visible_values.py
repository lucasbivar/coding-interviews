"""
Given a binary tree return all the values you’d be able to 
see if you were standing on the left side of it with 
values ordered from top to bottom.

Ex: Given the following tree…

-->    4
      / \
-->  2   7
return [4, 2]


Ex: Given the following tree…

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
"""

from typing import Deque, Optional, List
from collections import deque

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def visibleValues(root: Optional[TreeNode]) -> List[int]:
  # Time: O(n)
  # Space: O(n)
  if not root: return []
  
  output: List[int] = []

  currLevel: Deque[TreeNode] = deque()
  currLevel.append(root)
  
  while len(currLevel) != 0:
    output.append(currLevel[0].data)
    nextLevel: Deque[TreeNode] = deque()

    while len(currLevel) != 0:
      currNode: TreeNode = currLevel.popleft()

      if currNode.left:
        nextLevel.append(currNode.left)
      
      if currNode.right:
        nextLevel.append(currNode.right)

    
    currLevel = nextLevel
  
  return output



bt_1 = TreeNode(4)
bt_1.left = TreeNode(2)
bt_1.right = TreeNode(7)

assert visibleValues(bt_1) == [4, 2]


bt_2 = TreeNode(7)
bt_2.left = TreeNode(4)
bt_2.left.left = TreeNode(1)
bt_2.left.right = TreeNode(4)
bt_2.right = TreeNode(9)
bt_2.right.right = TreeNode(9)
bt_2.right.left = TreeNode(8)
bt_2.right.right.right = TreeNode(9)

assert visibleValues(bt_2) == [7, 4, 1, 9]


print("Passed all tests!")
