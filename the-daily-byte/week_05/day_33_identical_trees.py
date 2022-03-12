"""
Given two binary trees, return whether or not the two trees are identical. 
Note: identical meaning they exhibit the same structure and the same 
values at each node. 

Ex: Given the following trees...

        2
       / \
      1   3
    2
   / \
  1   3

return true.

Ex: Given the following trees...

        1
         \
          9
           \
           18
    1
   /
  9
   \
    18

return false.

Ex: Given the following trees...

        2
       / \
      3   1
    2
   / \
  1   3

return false.   

"""

class TreeNode:
  def __init__(self, v) -> None:
    self.value = v
    self.left = None
    self.right = None
  

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
  # Time: O(n)
  # Space: O(n)
  if not p and not q: return True

  if not p or not q: return False

  if p.value != q.value: return False

  return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


bt_1_p = TreeNode(2)
bt_1_p.left = TreeNode(1)
bt_1_p.right = TreeNode(3)

bt_1_q = TreeNode(2)
bt_1_q.left = TreeNode(1)
bt_1_q.right = TreeNode(3)

assert isSameTree(bt_1_p, bt_1_q) == True


bt_2_p = TreeNode(1)
bt_2_p.right = TreeNode(9)
bt_2_p.right.right = TreeNode(18)

bt_2_q = TreeNode(1)
bt_2_q.left = TreeNode(9)
bt_2_q.left.right = TreeNode(18)

assert isSameTree(bt_2_p, bt_2_q) == False


bt_3_p = TreeNode(2)
bt_3_p.left = TreeNode(3)
bt_3_p.right = TreeNode(1)

bt_3_q = TreeNode(2)
bt_3_q.left = TreeNode(1)
bt_3_q.right = TreeNode(3)


assert isSameTree(bt_3_p, bt_3_q) == False

print("Passed all tests!")