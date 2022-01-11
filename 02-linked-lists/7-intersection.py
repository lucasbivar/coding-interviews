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