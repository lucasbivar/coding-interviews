"""
Given a binary search tree, rearrange the tree such that it 
forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6

Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9


Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6

"""
global ll


class TreeNode:
  def __init__(self, v):
    self.val = v
    self.right = None
    self.left = None


def LLtoSTR(root):
  toStr = ""

  while root:
    toStr += str(root.val) 
    toStr += "->"
    root = root.right
  
  toStr += "null"

  return toStr


def inorderTraversal(root):
  global ll
  if not root: return 

  inorderTraversal(root.left)
  ll.left = None
  ll.right = root
  ll = root
  inorderTraversal(root.right)


def convertBSTtoLL(root):
  # Time: O(n)
  # Space: O(n)
  global ll

  dummyHead = TreeNode(-1)
  ll = dummyHead

  inorderTraversal(root)

  ll.left = None
  ll.right = None

  return dummyHead.right

bst_1 = TreeNode(5)
bst_1.left = TreeNode(1)
bst_1.right = TreeNode(6)

assert LLtoSTR(convertBSTtoLL(bst_1)) == "1->5->6->null"


bst_2 = TreeNode(5)
bst_2.left = TreeNode(2)
bst_2.right = TreeNode(9)
bst_2.left.left = TreeNode(1)
bst_2.left.right = TreeNode(3)

assert LLtoSTR(convertBSTtoLL(bst_2)) == "1->2->3->5->9->null"


bst_3 = TreeNode(5)
bst_3.right = TreeNode(6)

assert LLtoSTR(convertBSTtoLL(bst_3)) == "5->6->null"

print("Passed all tests!")