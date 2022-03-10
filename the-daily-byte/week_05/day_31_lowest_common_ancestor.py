"""
Given a binary search tree that contains unique values and two nodes 
within the tree, a, and b, return their lowest common ancestor.
Note: the lowest common ancestor of two nodes is the deepest node within 
the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.

Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.

Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
"""

class TreeNode:
  def __init__(self, v) -> None:
    self.val = v
    self.left = None
    self.right = None


def lowestCommonAncestor(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
  # Time: O(log n)
  # Space: O(1)

  currNode = root
  while currNode:
    if a.val > currNode.val and b.val > currNode.val:
      currNode = currNode.right
    elif a.val < currNode.val and b.val < currNode.val:
      currNode = currNode.left
    else:
      return currNode


bst_1 = TreeNode(7)
bst_1.left = TreeNode(2)
bst_1.right = TreeNode(9)
bst_1.left.left = TreeNode(1)
bst_1.left.right = TreeNode(5)

assert lowestCommonAncestor(bst_1, bst_1.left.left, bst_1.right) == bst_1


bst_2 = TreeNode(8)
bst_2.left = TreeNode(3)
bst_2.right =TreeNode(9)
bst_2.left.left = TreeNode(2)
bst_2.left.right = TreeNode(6)


assert lowestCommonAncestor(bst_2, bst_2.left.left, bst_2.left.right) == bst_2.left

bst_3 = TreeNode(8)
bst_3.left = TreeNode(6)
bst_3.right = TreeNode(9)

assert lowestCommonAncestor(bst_3, bst_3.left, bst_3) == bst_3


print("Passed all tests!")