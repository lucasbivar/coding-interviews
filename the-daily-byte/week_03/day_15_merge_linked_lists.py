"""
This question is asked by Apple. Given two sorted linked lists,
merge them together in ascending order and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

"""


class ListNode:
  def __init__(self, value):
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


def mergeLinkedLists(list1: ListNode, list2: ListNode) -> ListNode:
  # Time: O(m+n)
  # Space: O(1)
  dummyHead = ListNode(-1)
  mergedLL = dummyHead

  while list1 and list2:
    if list1.data <= list2.data:
      mergedLL.next = list1
      list1 = list1.next
    else:
      mergedLL.next = list2
      list2 = list2.next

    mergedLL = mergedLL.next
  
  mergedLL.next = list1 if list1 else list2

  return dummyHead.next


print("Test 01:")

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(6)

print(mergeLinkedLists(l1, l2))


print("Test 02:")

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

print(mergeLinkedLists(l1, l2))

print("Test 03:")

l1 = ListNode(4)
l1.next = ListNode(4)
l1.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(5)
l2.next.next = ListNode(6)

print(mergeLinkedLists(l1, l2))