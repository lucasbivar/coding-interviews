"""
Given a binary tree, return its column order traversal from top 
to bottom and left to right. Note: if two nodes are in the same 
row and column, order them from left to right.

Ex: Given the following tree…

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]


Ex: Given the following tree…

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""

from typing import Optional, List
from collections import deque
import heapq

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def gatherColumns(root: Optional[TreeNode]) -> List[List[int]]:
  if not root: return []
  
  nodeColumns = dict()
  
  queue = deque()
  queue.append((root, 0, 0)) #(node, row, columm)
  
  while len(queue) != 0:
    currNode, row, col = queue.popleft()
    
    if col not in nodeColumns:
      nodeColumns[col] = []
    
    heapq.heappush(nodeColumns[col], (row, currNode.data))
    
    if currNode.left:
      queue.append((currNode.left, row+1, col-1))
    
    if currNode.right:
      queue.append((currNode.right, row+1, col+1))
  
  output = []
  for j in range(min(nodeColumns), max(nodeColumns)+1):
    currCol = []
    while len(nodeColumns[j]) != 0:
      i, v = heapq.heappop(nodeColumns[j])
      currCol.append(v)
    
    output.append(currCol)
  
  return output


root_1 = TreeNode(8)
root_1.left = TreeNode(2)
root_1.right = TreeNode(29)
root_1.right.left = TreeNode(3)
root_1.right.right = TreeNode(9)

assert gatherColumns(root_1) == [[2], [8, 3], [29], [9]]


root_2 = TreeNode(100)
root_2.left = TreeNode(53)
root_2.left.left = TreeNode(32)
root_2.left.right = TreeNode(3)
root_2.right = TreeNode(78)
root_2.right.left = TreeNode(9)
root_2.right.right = TreeNode(20)

assert gatherColumns(root_2) == [[32], [53], [100, 3, 9], [78], [20]]


print("Passed all tests!")