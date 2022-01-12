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

  # Ex. 1
  # Input: l1 = [2,4,3], l2 = [5,6,4]
  # Output: [7,0,8]
  L1 = LinkedListNode(2)
  L1.next = LinkedListNode(4)
  L1.next.next = LinkedListNode(3)
  L2 = LinkedListNode(5)
  L2.next = LinkedListNode(6)
  L2.next.next = LinkedListNode(4)

  printLinkedList(L1)
  print("+")
  printLinkedList(L2)
  print("=")
  printLinkedList(func(L1, L2))
  print("-------------------------------")


  # Ex. 2
  # Input: l1 = [0], l2 = [0]
  # Output: [0]
  L1 = LinkedListNode(0)
  L2 = LinkedListNode(0)
  printLinkedList(L1)
  print("+")
  printLinkedList(L2)
  print("=")
  printLinkedList(func(L1, L2))
  print("-------------------------------")

  # Ex. 3
  # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
  # Output: [8,9,9,9,0,0,0,1]
  L1 = LinkedListNode(9)
  L1.next = LinkedListNode(9)
  L1.next.next = LinkedListNode(9)
  L1.next.next.next = LinkedListNode(9)
  L1.next.next.next.next = LinkedListNode(9)
  L1.next.next.next.next.next = LinkedListNode(9)
  L1.next.next.next.next.next.next = LinkedListNode(9)
  L2 = LinkedListNode(9)
  L2.next = LinkedListNode(9)
  L2.next.next = LinkedListNode(9)
  L2.next.next.next = LinkedListNode(9)


  printLinkedList(L1)
  print("+")
  printLinkedList(L2)
  print("=")
  printLinkedList(func(L1, L2))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Clarify Questions
# - Could the number be negative?
# - Are both numbers the same length?
# - Have I some memory limit? If yes, have I to solve with constant space complexity?
  
# Complexity:
# - Time: O(max(m, n)) -> m and represents the length of l1 and l2
# - Space: O(max(m, n)) 

# Create a new linked list with a dummy head. While at least one node 
# is different of None sum the nodes values and the carry, create a new
# node and add at the end of the new linked list. When the while loop
# finishes, if the carry is greater than zero create a new node with the value 
# and add it at the end of the new linked list. Return the dummyHead.next

def addTwoNumbers(l1, l2):
  dummyHead = LinkedListNode(0)
  p = l1
  q = l2
  curr = dummyHead
  carry = 0
  while p != None or q != None:
    x = p.val if p != None else 0
    y = q.val if q != None else 0
    digitSum = carry + x + y
    carry = digitSum//10
    curr.next = LinkedListNode(digitSum%10)
    curr = curr.next
    if p != None: p = p.next
    if q != None: q = q.next
  
  if carry > 0:
    curr.next = LinkedListNode(carry)
  
  return dummyHead.next

tests(addTwoNumbers)

# Approach #2
# - Time: O(max(m, n)) -> m and represents the length of l1 and l2
# - Space: O(1) 
def addRemaingDigits(lastNode, carry):
  lastNode = lastNode.next
  while carry != 0:
    currentDigitSum = lastNode.val + carry
    carry = currentDigitSum//10
    currentDigitSum = currentDigitSum%10
    lastNode.val = currentDigitSum
    if lastNode.next == None and carry != 0:
      lastNode.next = LinkedListNode(carry)
      carry = 0
    lastNode = lastNode.next
                
def addTwoNumbers(l1, l2):
  carry = 0
  currentL1 = l1
  currentL2 = l2
  
  while currentL1.next != None and currentL2.next != None:
    currentDigitSum = currentL1.val + currentL2.val + carry

    carry = currentDigitSum//10
    currentDigitSum = currentDigitSum%10
    
    currentL1.val = currentDigitSum
    currentL2.val = currentDigitSum
    
    currentL1 = currentL1.next
    currentL2 = currentL2.next
  
  currentDigitSum = currentL1.val + currentL2.val + carry
  carry = currentDigitSum//10
  currentDigitSum = currentDigitSum%10
  
  currentL1.val = currentDigitSum
  currentL2.val = currentDigitSum
  
  if currentL1.next == None and currentL2.next == None:
    if carry != 0:
      currentL1.next = LinkedListNode(carry)
    return l1
  elif currentL1.next == None:
    addRemaingDigits(currentL2, carry)
    return l2
  else:
    addRemaingDigits(currentL1, carry)
    return l1 

tests(addTwoNumbers)
