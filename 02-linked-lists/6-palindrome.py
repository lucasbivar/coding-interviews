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

# Clarify Questions
# - Could the linked list have an odd or even length? Yes!
# - Have I some limit memory? Is it necessary solve with constant space complexity?
# - Have I the linked list length? No!
# - Should I return True if the list is empty?

# Approach #1
# Two pointer and stack

# 1. Use two pointers (fast and slow) to find the middle of the linked list
# 2. Every time that we move the slow pointer we add the node value in the stack
# 3. When we find the middle of the list, start to pop the stack and iterate through
#    the remaining nodes, compare if the popped value is equal to the current node. 
#    If it's different, the linked list is not a palindrome

# | = fast; ^ = slow

# stack = [1]
# 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
# ^|

# stack = [1, 2]
# 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
#      ^    |

# stack = [1, 2, 3]
# 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
#           ^         |

# stack = [1, 2, 3] (if the fast pointer is equal to the end, don't add the slow in the stack)
# 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
#                ^              |


# Complexity:
# - Time: O(n) -> n is the linked list length
# - Space: O(n/2) = O(n)

def isPalindrome(head):
  if head == None or head.next == None: return True
  fast = head
  slow = head
  stack = []
  while fast != None and fast.next != None:
    fast = fast.next.next
    stack.append(slow.val)
    slow = slow.next
    if fast != None and fast.next == None: # the list has odd size
      slow = slow.next

  while slow:
    if slow.val != stack[-1]:
      return False
    
    slow = slow.next
    stack.pop()
  return True

# Ex. 1
# Input: head = [1,2,3,4,3,2,1]
# Output: true
L1 = LinkedListNode(1)
L1.next = LinkedListNode(2)
L1.next.next = LinkedListNode(3)
L1.next.next.next = LinkedListNode(4)
L1.next.next.next.next = LinkedListNode(3)
L1.next.next.next.next.next = LinkedListNode(2)
L1.next.next.next.next.next.next = LinkedListNode(1)
printLinkedList(L1)
print("Is palindrome? ", isPalindrome(L1))
print("~~~~~~~~")

# Ex. 2
# Input: head = [1,2]
# Output: false
L1 = LinkedListNode(1)
L1.next = LinkedListNode(2)

printLinkedList(L1)
print("Is palindrome? ", isPalindrome(L1))
print("~~~~~~~~")

# Ex. 3
# Input: head = [1,2,2,1]
# Output: true
L1 = LinkedListNode(1)
L1.next = LinkedListNode(2)
L1.next.next = LinkedListNode(2)
L1.next.next.next = LinkedListNode(1)

printLinkedList(L1)
print("Is palindrome? ", isPalindrome(L1))
print("~~~~~~~~")