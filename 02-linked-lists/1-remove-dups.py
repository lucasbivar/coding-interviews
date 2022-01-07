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


# Complexity:
# Time: O(n)
# Space: O(1)

def removeDups(head):
    if head == None: return head
    
    dummyHead = LinkedListNode(1 if head.value == 0 else 0)
    dummyHead.next = head
    
    previousNode = dummyHead
    currentNode = dummyHead.next
    
    lastUnduplicatedNode = dummyHead
    
    while currentNode != None and currentNode.next != None:
        if currentNode.value != previousNode.value and currentNode.value != currentNode.next.value:
            lastUnduplicatedNode.next = currentNode
            lastUnduplicatedNode = lastUnduplicatedNode.next
        
        previousNode = currentNode
        currentNode = currentNode.next
    
    if previousNode.value != currentNode.value:
        lastUnduplicatedNode.next = currentNode
        lastUnduplicatedNode = lastUnduplicatedNode.next
    
    lastUnduplicatedNode.next = None
    
    return dummyHead.next

# Ex: list: 1->2->2->2->3->4->None | return 1->3->4->None
LList = LinkedListNode(1)
LList.next = LinkedListNode(2)
LList.next.next = LinkedListNode(2)
LList.next.next.next = LinkedListNode(2)
LList.next.next.next.next = LinkedListNode(3)
LList.next.next.next.next.next = LinkedListNode(4)

printLinkedList(LList)
printLinkedList(removeDups(LList))

# Ex: list: 2->2->2->None | return None
LList = LinkedListNode(2)
LList.next = LinkedListNode(2)
LList.next.next = LinkedListNode(2)

printLinkedList(LList)
printLinkedList(removeDups(LList))