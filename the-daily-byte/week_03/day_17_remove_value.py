"""
This question is asked by Google. Given a linked list and a value,
remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
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

def removeValue(head: ListNode, value: int) -> ListNode:
  # Time: O(n)
  # Space: O(1)
  if not head: return None

  dummyHead = ListNode(-1)
  dummyHead.next = head

  currNode = dummyHead
  while currNode and currNode.next:
    if currNode.next.data == value:
      currNode.next = currNode.next.next
    else:
      currNode = currNode.next

  return dummyHead.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

assert str(removeValue(l1, 3)) == "1->2->null"


l2 = ListNode(8)
l2.next = ListNode(1)
l2.next.next = ListNode(1)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(12)

assert str(removeValue(l2, 1)) == "8->4->12->null"


l3 = ListNode(7)
l3.next = ListNode(12)
l3.next.next = ListNode(2)
l3.next.next.next = ListNode(9)

assert str(removeValue(l3, 7)) == "12->2->9->null"

print("Passed all tests!")
