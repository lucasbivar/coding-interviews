"""
This question is asked by Microsoft. Given a linked list, 
containing unique numbers, return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points 
back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
"""
class ListNode:
  def __init__(self, value=None):
    self.data = value
    self.next = None
  
  def __str__(self) -> str:
      toString = ""
      currNode = self

      while currNode:
        toString += str(currNode.data)
        toString += "->"
        currNode = currNode.next

      
      toString += "null"

      return toString

  
def hasCycle(head: ListNode) -> bool:
  # Time: O(n)
  # Space: O(n)

  seen = set()
  currNode = head

  while currNode:
    if currNode in seen:
      return True
    
    seen.add(currNode)
    currNode = currNode.next
  
  return False


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = l1

assert hasCycle(l1) == True

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

assert hasCycle(l2) == False

l3 = ListNode(1)
l3.next = l3

assert hasCycle(l3) == True

print("Passed all tests!")

# Two pointers:
# - | : slow pointer
# - ^ : fast pointer

# 1 -> 2 -> 3 -> 4 -> 1 (first node)
# |    ^

# 1 -> 2 -> 3 -> 4 -> 1 (first node)
#      |         ^

# 1 -> 2 -> 3 -> 4 -> 1 (first node)
#      ^    |         

# 1 -> 2 -> 3 -> 4 -> 1 (first node)
#                |    
#                ^ -> cycle found
  
def hasCycle(head: ListNode) -> bool:
  # Time: O(n)
  # Space: O(1)
  if not head: return False
  
  slow = head
  fast = head.next

  while fast and fast.next:
    if slow == fast:
      return True

    slow = slow.next
    fast = fast.next.next
  
  return False


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = l1

assert hasCycle(l1) == True

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

assert hasCycle(l2) == False

l3 = ListNode(1)
l3.next = l3

assert hasCycle(l3) == True

print("Passed all tests!")