"""
Given a binary tree, return a list of strings containing all root to leaf paths.

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]


Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
"""

from typing import List, Optional

class TreeNode:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None


def buildPaths(root: Optional[TreeNode], currState: List[int], allPaths: List[str]) -> None:
  
  currState.append(str(root.data))

  if not root.left and not root.right:
    allPaths.append("->".join(currState))
    return
  
  if root.left:
    buildPaths(root.left, currState, allPaths)
    currState.pop()

  
  if root.right:
    buildPaths(root.right, currState, allPaths)
    currState.pop()



def rootToleafPaths(root: Optional[TreeNode]) -> List[str]:
  # Time: O(n)
  # Space: O(n)
  if not root: return []

  output = []

  buildPaths(root, [], output)

  return output


root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.right = TreeNode(3)

assert rootToleafPaths(root_1) == ['1->2', '1->3']


root_2 = TreeNode(8)
root_2.left = TreeNode(2)
root_2.right = TreeNode(29)
root_2.right.left = TreeNode(3)
root_2.right.right = TreeNode(9)

assert rootToleafPaths(root_2) == ["8->2", "8->29->3", "8->29->9"]


root_3 = TreeNode(1)
root_3.left = TreeNode(2)
root_3.right = TreeNode(3)
root_3.left.right = TreeNode(5)

assert rootToleafPaths(root_3) == ["1->2->5","1->3"]


print("Passed all tests!")

