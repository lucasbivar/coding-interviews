"""
This question is asked by Facebook. Given a linked list and 
a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
"""

class ListNode:
  def __init__(self, value=None):
    self.data = value
    self.next = None

  def __str__(self) -> str:
    llString = ""
    currNode = self

    while currNode:
      llString += (str(currNode.data)+"->")
      currNode = currNode.next
    
    llString += "null"

    return llString
    

def removeNthToLastNode(head: ListNode, n: int) -> ListNode:
  if not head: return None
  # Time: O(m)
  # Space: O(1)
  dummyHead = ListNode(-1)
  dummyHead.next = head

  fast = dummyHead
  for _ in range(0, n):
    fast = fast.next
  
  slow = dummyHead
  while fast.next:
    fast = fast.next
    slow = slow.next
  
  slow.next = slow.next.next
  return dummyHead.next
  

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert str(removeNthToLastNode(l1, 1)) == "1->2->null"

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert str(removeNthToLastNode(l1, 2)) == "1->3->null"


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert str(removeNthToLastNode(l1, 3)) == "2->3->null"