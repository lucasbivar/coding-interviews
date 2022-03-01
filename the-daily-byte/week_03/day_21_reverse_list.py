"""
This question is asked by Facebook. Given a linked list, containing unique values, 
reverse it, and return the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which points to a 
list that looks like the following: 3->2->1->null

7->15->9->2->null, return a reference to the node that contains 2 which 
points to a list that looks like the following: 2->9->15->7->null

1->null, return a reference to the node that contains 1 which points to a 
list that looks like the following: 1->null
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

def reverseList(head):
  # Time: O(n)
  # Space: O(1)
  if not head: return None

  currNode = head
  newHead = None

  while currNode:
    tmp = currNode.next
    currNode.next = newHead
    newHead = currNode
    currNode = tmp

  return newHead


# Ex.: 1
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert str(reverseList(l1)) == "3->2->1->null"

# Ex.: 2
l2 = ListNode(7)
l2.next = ListNode(15)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(2)

assert str(reverseList(l2)) == "2->9->15->7->null"


# Ex.: 3
l3 = ListNode(1)
assert str(reverseList(l3)) == "1->null"

print("Passed all tests!")