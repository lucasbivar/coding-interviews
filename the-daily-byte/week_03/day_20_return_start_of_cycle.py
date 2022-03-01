"""
This question is asked by Apple. Given a potentially cyclical 
linked list where each value is unique, return the node at which 
the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
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
    
    toString += "null"

    return toString


def startOfCycle(head) -> ListNode:
  # Time: O(n)
  # Space: O(n)
  if not head: return None

  seen = set()
  currNode = head

  while currNode:
    if currNode in seen:
      return currNode

    seen.add(currNode)
    currNode = currNode.next
  
  return None

# Ex. 1:
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
assert startOfCycle(l1) == None

# Ex. 2:
l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = l2.next

assert startOfCycle(l2) == l2.next

# Ex. 3:
l3 = ListNode(1)
l3.next = ListNode(9)
l3.next.next = ListNode(3)
l3.next.next.next = ListNode(7)
l3.next.next.next.next = l3.next.next.next

assert startOfCycle(l3) == l3.next.next.next

def startOfCycle(head) -> ListNode:
  # Time: O(n)
  # Space: O(1)
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      slow = head
      while slow != fast:
        slow = slow.next
        fast = fast.next
      return slow

  return None


# Ex. 1:
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
assert startOfCycle(l1) == None

# Ex. 2:
l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = l2.next

assert startOfCycle(l2) == l2.next

# Ex. 3:
l3 = ListNode(1)
l3.next = ListNode(9)
l3.next.next = ListNode(3)
l3.next.next.next = ListNode(7)
l3.next.next.next.next = l3.next.next.next

assert startOfCycle(l3) == l3.next.next.next