"""
Given a binary search tree, return its mode (you may assume 
the answer is unique). If the tree is empty, return -1. Note: 
the mode is the most frequently occurring value in the tree.


Ex: Given the following tree...

        2
       / \
      1   2
return 2.


Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
"""

from typing import Optional
from collections import deque
from math import inf

class TreeNode:
  def __init__(self, v) -> None:
    self.data = v
    self.left = None
    self.right = None


def findTheMode(root: Optional[TreeNode]) -> int:
  # Time: O(n)
  # Space: O(n + m)

  # n -> number of nodes
  # m -> number of different values

  if not root: return -1

  queue = deque()
  queue.append(root)

  countValues = dict()
  
  while len(queue) != 0:
    currNode = queue.popleft()
    
    if currNode.data not in countValues:
      countValues[currNode.data] = 0
    
    countValues[currNode.data] += 1

    if currNode.left:
      queue.append(currNode.left)

    if currNode.right:
      queue.append(currNode.right)
  
  mostFrequentlyValue = None
  maxValue = -inf

  for k, v in countValues.items():
    if v > maxValue:
      mostFrequentlyValue = k
      maxValue = v

  return mostFrequentlyValue


bst_1 = TreeNode(2)
bst_1.left = TreeNode(1)
bst_1.right = TreeNode(2)

assert findTheMode(bst_1) == 2


bst_2 = TreeNode(7)
bst_2.left = TreeNode(4)
bst_2.left.left = TreeNode(1)
bst_2.left.right = TreeNode(4)
bst_2.right = TreeNode(9)
bst_2.right.left = TreeNode(8)
bst_2.right.right = TreeNode(9)
bst_2.right.right.right = TreeNode(9)

assert findTheMode(bst_2) == 9

print("Passed all tests!")