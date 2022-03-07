"""
This question is asked by Google. Given the reference to the root of a 
binary search tree and a search value, return the reference to the node that 
contains the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the following tree...

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the following tree...

        8
       / \
      6   9
and the search value 7 return null.
"""

class TreeNode:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

  
def findValue(head: TreeNode, x: int) -> TreeNode:
  # Time: O(n) or O(log n) if the tree is balanced
  # Space: O(n) or O(h) if the tree is balanced

  if not head: return None

  if head.data == x:
    return head
  
  if x < head.data:
    return findValue(head.left, x)

  return findValue(head.right, x)


bst_1 = TreeNode(3)
bst_1.left = TreeNode(1)
bst_1.right = TreeNode(4)

assert findValue(bst_1, 1) == bst_1.left


bst_2 = TreeNode(7)
bst_2.left = TreeNode(5)
bst_2.right = TreeNode(9)
bst_2.right.left = TreeNode(8)
bst_2.right.right = TreeNode(10)

assert findValue(bst_2, 9) == bst_2.right


bst_3 = TreeNode(8)
bst_3.left = TreeNode(6)
bst_3.right = TreeNode(9)

assert findValue(bst_3, 7) == None

print("Passed all tests!")