class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

def printLinkedList(linked_list):
    linked_list_str = ""
    while linked_list != None:
        linked_list_str += str(linked_list.value) + "->"
        linked_list=linked_list.next
   
    linked_list_str += "None"
    print(linked_list_str)

def tests(func):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
  #Ex. 1: list 1->2->3->4->None, K = 1 | return 4
  LList = LinkedListNode(1)
  LList.next = LinkedListNode(2)
  LList.next.next = LinkedListNode(3)
  LList.next.next.next = LinkedListNode(4)

  printLinkedList(LList)
  print("Kth To Last:", func(LList, 1))
  print("-------------------------------")

  #Ex. 2: list 1->2->3->4->None, K = 2 | return 3
  LList = LinkedListNode(1)
  LList.next = LinkedListNode(2)
  LList.next.next = LinkedListNode(3)
  LList.next.next.next = LinkedListNode(4)

  printLinkedList(LList)
  print("Kth To Last:", func(LList, 2))
  print("-------------------------------")

  #Ex. 3: list 1->2->3->4->None, K = 3 | return 2
  LList = LinkedListNode(1)
  LList.next = LinkedListNode(2)
  LList.next.next = LinkedListNode(3)
  LList.next.next.next = LinkedListNode(4)

  printLinkedList(LList)
  print("Kth To Last:", func(LList, 3))
  print("-------------------------------")

  #Ex. 3: list 1->2->3->4->None, K = 5 | return None
  LList = LinkedListNode(1)
  LList.next = LinkedListNode(2)
  LList.next.next = LinkedListNode(3)
  LList.next.next.next = LinkedListNode(4)

  printLinkedList(LList)
  print("Kth To Last:", func(LList, 5))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Clarify questions
# Can K be greater than linked list size? If yes, when we go to assign the 
# p2 node reference we have to deal with it returning None, but in this case,
# is not necessary, K will be always less or equal than the linked list size

# Can the linked list be empty? Yes

# Is the size of the list known? No

# Should I return the node or the node value? In this case, I'm returning the node value

# Approach #1 
# Recursive 

# Complexity:
# Time: O(n)
# Space: O(n)

def printKthToLast(head, K):
  if head == None:
    return 0
  
  index = printKthToLast(head.next, K)+1

  if index == K:
    print(str(K)+"th to last node is "+str(head.value))

  return index

#Ex. 1: list 1->2->3->4->None, K = 1 | return 4
LList = LinkedListNode(1)
LList.next = LinkedListNode(2)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(4)

printLinkedList(LList)
printKthToLast(LList, 1)

#Ex. 2: list 1->2->3->4->None, K = 2 | return 3
LList = LinkedListNode(1)
LList.next = LinkedListNode(2)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(4)

printLinkedList(LList)
printKthToLast(LList, 2)

#Ex. 3: list 1->2->3->4->None, K = 3 | return 2
LList = LinkedListNode(1)
LList.next = LinkedListNode(2)
LList.next.next = LinkedListNode(3)
LList.next.next.next = LinkedListNode(4)

printLinkedList(LList)
printKthToLast(LList, 3)


# Approach #2
# two pointers
# p1 = ^ and p2 = |

# 1->2->3->4->5->6->none (k = 3)
# ^     |
# 1->2->3->4->5->6->none (k = 3)
#    ^     |
# 1->2->3->4->5->6->none (k = 3)
#       ^     |
# 1->2->3->4->5->6->none (k = 3)
#          ^     | (p2.next = None -> end, so return the p1 value)

# Complexity:
# Time: O(n)
# Space: O(1)

def getKthToLast(head, K):
  if head == None:
    return None
  
  pointer1 = head
  pointer2 = head
  for i in range(1, K):
    if pointer2.next == None: return None

    pointer2 = pointer2.next
  
  while pointer2.next:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  
  return pointer1.value

tests(getKthToLast)


