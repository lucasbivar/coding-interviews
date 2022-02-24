"""
This question is asked by Amazon. Given a non-empty linked list, 
return the middle node of the list. If the linked list contains
an even number of elements, return the node closer to the end.
Ex: Given the following linked lists...

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
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
    

def findMiddleElement(head: ListNode) -> int:
  # Time: O(n)
  # Space: O(1)
  if not head: return -1

  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  return slow.data

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert findMiddleElement(l1) == 2

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)

assert findMiddleElement(l2) == 3


l3 = ListNode(1)

assert findMiddleElement(l3) == 1

print("Passed all tests!")