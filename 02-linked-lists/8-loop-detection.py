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
  # Input: head = [3,2,0,-4], pos = 1
  # Output: tail connects to node with value 2
  L1 = LinkedListNode(3)
  L1.next = LinkedListNode(2)
  L1.next.next = LinkedListNode(0)
  L1.next.next.next = LinkedListNode(-4)
  L1.next.next.next.next = L1.next
  print(f"Tail connects to node with value {func(L1).val if func(L1) else None}")
  print("-------------------------------")

  # Ex. 2
  # Input: head = [1,2], pos = 0
  # Output: tail connects to node with value 1
  L1 = LinkedListNode(1)
  L1.next = LinkedListNode(2)
  L1.next.next = L1
  print(f"Tail connects to node with value {func(L1).val if func(L1) else None}")
  print("-------------------------------")
  # Ex. 3
  # Input: head = [1], pos = -1
  # Output: tail connects to node with value None
  L1 = LinkedListNode(1)
  if not func(L1):
    print("No cycle")
  else:
    print("Wrong Answer!")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Approach #1
# Iterate through each node:
# 1. check if the current node is in the visited nodes set.
#    if yes, return the node, once this node is the beginning of the cycle
# 2. add in a hash set and go to the next node

# If we iterate through all nodes and don't find any repeated nodes, the linked
#    list doesn't have cycle

# Complexity:
# Time: O(n) -> n is the size of the linked list without cycle or the size until repating the cycle
# Space: O(n)

def detectCycle(head):
  visitedNodes = set()
  currentNode = head
  while currentNode != None:
    if currentNode in visitedNodes:
      return currentNode
    
    visitedNodes.add(currentNode)
    currentNode = currentNode.next
  
  return None

tests(detectCycle)


# Approach #2
# Using the 2 pointers (slow, fast) approach we will find a collision if it exists.

# When we find the collision, if we move a pointer to the head and one at the collision,
# when they meet they'll meet at the beginning of the loop.

# Complexity:
# Time: O(n) -> n is the size of the linked list without cycle or the size until repating the cycle
# Space: O(1)

def detectCycle(head):
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      slow = head
      while slow != fast:
        slow = slow.next
        fast = fast.next
      return slow

  return None

tests(detectCycle)