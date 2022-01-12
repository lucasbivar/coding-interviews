class LinkedListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def printLinkedList(linked_list):
    linked_list_str = ""
    while linked_list != None:
        linked_list_str += str(linked_list.val) + "->"
        linked_list=linked_list.next
   
    linked_list_str += "None"
    print(linked_list_str)

def tests(func):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  # Ex.: 1
  # Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
  # Output: Intersected at '8'
  L1 = LinkedListNode(4)
  L1.next = LinkedListNode(1)
  L1.next.next = LinkedListNode(8)
  L1.next.next.next = LinkedListNode(4)
  L1.next.next.next.next = LinkedListNode(5)

  L2 = LinkedListNode(5)
  L2.next = LinkedListNode(6)
  L2.next.next = LinkedListNode(1)
  L2.next.next.next = L1.next.next
  L2.next.next.next.next = L1.next.next.next
  L2.next.next.next.next.next = L1.next.next.next.next

  printLinkedList(L1)
  printLinkedList(L2)
  print(f"Intersected at {func(L1, L2).val if func(L1, L2) else None}")
  print("-------------------------------")

  # Ex.: 2
  # Input: listA = [1,9,1,2,4], listB = [3,2,4]
  # Output: Intersected at '2'
  L1 = LinkedListNode(1)
  L1.next = LinkedListNode(9)
  L1.next.next = LinkedListNode(1)
  L1.next.next.next = LinkedListNode(2)
  L1.next.next.next.next = LinkedListNode(4)

  L2 = LinkedListNode(3)
  L2.next = L1.next.next.next 
  L2.next.next = L1.next.next.next.next

  printLinkedList(L1)
  printLinkedList(L2)
  print(f"Intersected at {func(L1, L2).val if func(L1, L2) else None}")
  print("-------------------------------")

  # Ex.: 3
  # listA = [2,6,4], listB = [1,5]
  # Output: No intersection
  L1 = LinkedListNode(2)
  L1.next = LinkedListNode(6)
  L1.next.next = LinkedListNode(4)

  L2 = LinkedListNode(1)
  L2.next = LinkedListNode(5)

  printLinkedList(L1)
  printLinkedList(L2)
  print(f"Intersected at {func(L1, L2).val if func(L1, L2) else None}")

  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  
# Clarify questions
# - Have I some memory limit?
# - Could the linked list be empty?
# - Could both linked lists have different sizes?
# - Could there be no intersection between the lists?

# Approach #1
# Iterate through the linked list A and add the references in a hash set
# Iterate through the linked list B and check if the current node's reference is in the hash set
# Complexity:
# Time: O(n+m)
# Spacee: O(n)

def getIntersectionNode(headA, headB):
  if not headA or not headB: return None
  aReferences = set()
  pointerA = headA
  while pointerA != None:
    aReferences.add(pointerA)
    pointerA = pointerA.next
  
  pointerB = headB
  while pointerB != None:
    if pointerB in aReferences:
      return pointerB
    
    pointerB = pointerB.next
  
  return None

tests(getIntersectionNode)

# Approach #2
# While both pointers from list A and B are different. 
# If either pointer hits the end, switch to the other head and continue the second traversal, 
# if not hit the end, just move on to next
# Complexity:
# Time: O(n+m)
# Space: O(1)

def getIntersectionNode(headA, headB):
  if not headA or not headB: return None

  pointerA = headA 
  pointerB = headB

  while pointerA != pointerB:
      pointerA = headB if not pointerA else pointerA.next
      pointerB = headA if not pointerB else pointerB.next

  return pointerA

tests(getIntersectionNode)
