"""
Given an array of numbers sorted in ascending order, return a 
height-balanced binary search tree using every number from the array.
Note: height-balanced meaning that the level of any node’s two subtrees 
should not differ by more than one.

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
"""
from math import floor
from aux import printTree
from typing import List

class TreeNode:
  def __init__(self, v) -> None:
    self.value = v
    self.left = None
    self.right = None


def build(arr: List[int], begin: int, end: int) -> TreeNode:
  if begin > end: return None

  middlePos = floor((begin+end)/2)

  currNode = TreeNode(arr[middlePos])
  currNode.left = build(arr, begin, middlePos-1)
  currNode.right = build(arr, middlePos+1, end)

  return currNode

def sortedArrToBST(arr: List[int]) -> TreeNode:
  # Time: O(n)
  # Space: O(log n)
  if len(arr) == 0: return None

  return build(arr, 0, len(arr)-1)


arr_1 = [1, 2, 3]
bst_1 = sortedArrToBST(arr_1)

printTree(bst_1, None, False)

print()
print("---------------------")
print()

arr_2 = [1,2,3,4,5,6]
bst_2 = sortedArrToBST(arr_2)

printTree(bst_2, None, False)

