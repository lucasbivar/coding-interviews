"""
Design a class to implement a stack using only a single queue. Your class, 
QueueStack, should support the following stack methods: push() (adding an item), 
pop() (removing an item), peek() (returning the top value without removing it), 
and empty() (whether or not the stack is empty).
"""
from collections import deque

class QueueStack:
  # Space: O(n)
  # Time: push -> O(n) | pop - peek - empty -> O(1)

  def __init__(self):
    self.queue = deque()
  
  def push(self, item):
    numberOfSwaps = len(self.queue)

    self.queue.append(item)

    for _ in range(numberOfSwaps):
      self.queue.append(self.queue.popleft())


  def pop(self):
    return self.queue.popleft()

  def peek(self):
    return self.queue[0]

  def empty(self):
    return True if len(self.queue) == 0 else False

stack = QueueStack()

print(stack.empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
stack.pop()

print(stack.peek())
print(stack.empty())
