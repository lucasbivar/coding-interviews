class LinkedListNode:
  def __init__(self, val):
    self.value = val
    self.next = None

def printLinkedList(linked_list):
    linked_list_str = ""
    while linked_list != None:
        linked_list_str += str(linked_list.value) + "->"
        linked_list=linked_list.next
   
    linked_list_str += "None"
    print(linked_list_str)

# Clarify questions:
# - Are all numbers positive? No, the number can be both
# - Could the list be empty? Yes
# - Have I some memory limit? No
# - Does the elements' order matter? No, it doesn't. You just need to put 
# the elements with value less than X first.

# Approach #1
# 1. Create a dummy head
# 2. Create three pointer:
#   slow = to store the reference of the last node less than X that is in the beginning of the list
#   fast = to find the node with value less than X
#   prevFast = to help remove the fast node found with a value less than X

# 3. Use the fast pointer to iterate over the entire list, if find a node with a value
# less than X, remove this node using prevFast and add it in front of the node stored 
# in slow the pointer

# 4. Return dummyHead.next

# Complexity:
# - Time: O(n)
# - Space: O(1)

def partition(head, x):
  if head == None: return None
  dummyHead = LinkedListNode(1 if head.value == 0 else 0)
  dummyHead.next = head

  slow = dummyHead
  prevFast = dummyHead
  fast = head
  while fast:
    if fast.value < x:
      prevFast.next = fast.next

      fast.next = slow.next
      slow.next = fast
      slow = fast

    prevFast = fast
    fast = fast.next
  
  return dummyHead.next

#Ex. 1: list 1->4->3->5->2->None, X = 2 | return 1->4->3->5->2->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 1", end=" |")
printLinkedList(partition(LList, 1))

#Ex. 2: list 1->4->3->5->2->None, X = 4 | return 1->3->2->4->5->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 4", end=" |")
printLinkedList(partition(LList, 4))

#Ex. 3: list 1->4->3->5->2->None, X = 5 | return 1->4->3->2->5->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 5", end=" |")
printLinkedList(partition(LList, 5))
print("-------------")

# Approach #2
# 1. Create two linked lists
#   greaterOrEqual = store the nodes with a value greater or equal than X
#   less = store the node with a value less than X
# 2. Join the end of the small list with the beginnig of the big list

# linked list: 1 -> 6 -> 8 -> 3 -> 5 -> 2 -> None | X = 5
# less: 1 -> 3 -> 2 -> None
# greaterOrEqual: 6 -> 8 -> 5 -> None

#  less -> greaterOrEqual -> None
# 1 -> 3 -> 2 -> 6 -> 8 -> 5 -> None

# Complexity:
# - Time: O(n)
# - Space: O(1) - we have not utilized any extra space, 
# the point to note is that we are reforming the original 
# list, by moving the original nodes, we have not used any extra space as such.

def partition(head, x):
  if head == None: return None
  less = LinkedListNode(0)
  lessBegin = less
  greaterOrEqual = LinkedListNode(0)
  greaterOrEqualBegin = greaterOrEqual

  while head:
    if head.value < x:
      less.next = head
      less = head
    else:
      greaterOrEqual.next = head
      greaterOrEqual = head

    head = head.next
  
  less.next = greaterOrEqualBegin.next
  greaterOrEqual.next = None

  return lessBegin.next

#Ex. 1: list 1->4->3->5->2->None, X = 2 | return 1->4->3->5->2->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 1", end=" |")
printLinkedList(partition(LList, 1))

#Ex. 2: list 1->4->3->5->2->None, X = 4 | return 1->3->2->4->5->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 4", end=" |")
printLinkedList(partition(LList, 4))

#Ex. 3: list 1->4->3->5->2->None, X = 5 | return 1->4->3->2->5->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(4)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(5)
LList.next.next.next.next = LinkedListNode(2)

printLinkedList(LList)
print("X = 5", end=" |")
printLinkedList(partition(LList, 5))
print("-------------")