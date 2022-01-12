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

  # Ex. 1: "a"->"b"->"c"->"d"->none, node "c" | new list: "a"->"b"->"d"->none
  LList = LinkedListNode("a")
  LList.next = LinkedListNode("b")
  LList.next.next = LinkedListNode("c")
  LList.next.next.next = LinkedListNode("d")

  printLinkedList(LList)
  print(func(LList.next.next))
  printLinkedList(LList)

  # Ex. 2: "a"->"b"->"c"->"d"->"e"->none, node "b" | new list: "a"->"c"->"d"->"e"->none
  LList = LinkedListNode("a")
  LList.next = LinkedListNode("b")
  LList.next.next = LinkedListNode("c")
  LList.next.next.next = LinkedListNode("d")
  LList.next.next.next.next = LinkedListNode("e")

  printLinkedList(LList)
  print(func(LList.next))
  printLinkedList(LList)


# Clarify Questions
# - Should I treat if the node is equal to None or the node is the last?
# - Could I return a boolean value based on the operation's result?

# Approach #1
# If we have access the linked list we could iterate through the list
# using previousNode and currentNode until currentNode reference be equal to
# the node reference, so we just next to assing the node.next to prev.next

# Complexity:
# - Time: O(n) 
# - Space: O(1)

# Approach #2
# 1. Assign the next node value to the current node
# 2. Assign the node.next.next to node.next
# 1 -> 2 -> 3 -> 4  (Node val = 2)

# 1 -> 2 -> 3 -> 4  
# 1 -> 3 -> 3 -> 4  
# 1 -> 3 -> 4  

# Complexity:
# - Time: O(1) 
# - Space: O(1)

def deleteMiddleNode(node: LinkedListNode) -> bool:
  if node == None or node.next == None: return False

  node.value = node.next.value
  node.next = node.next.next

  return True

tests(deleteMiddleNode)