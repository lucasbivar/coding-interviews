"""
Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]

Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""

from typing import List, Optional
from collections import deque

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.children = []


def gatherN_arrTreeLevels(root: Optional[TreeNode]) -> List[List[int]]:
  # Time: O(n)
  # Space: O(n)
  if not root: return []

  output = deque()

  currLevel = deque()
  currLevel.append(root)


  while len(currLevel) != 0:
    nextLevel = deque()
    currNodesValues = []

    while len(currLevel) != 0:
      currNode = currLevel.popleft()
      currNodesValues.append(currNode.data)

      for child in currNode.children:
        nextLevel.append(child)
    
    currLevel = nextLevel
    output.append(currNodesValues)

  return list(output)



root_1 = TreeNode(8)
root_1.children.append(TreeNode(2))
root_1.children.append(TreeNode(3))
root_1.children.append(TreeNode(29))

assert gatherN_arrTreeLevels(root_1) == [[8], [2, 3, 29]]


root_2 = TreeNode(2)
root_2.children.append(TreeNode(1))
root_2.children[0].children.append(TreeNode(8))
root_2.children.append(TreeNode(6))
root_2.children[1].children.append(TreeNode(2))
root_2.children[1].children[0].children.append(TreeNode(19))
root_2.children[1].children[0].children.append(TreeNode(12))
root_2.children[1].children[0].children.append(TreeNode(90))
root_2.children.append(TreeNode(9))
root_2.children[2].children.append(TreeNode(2))

assert gatherN_arrTreeLevels(root_2) == [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]


print("Passed all tests!")