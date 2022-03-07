"""
This question is asked by Microsoft. Design a class, MovingAverage, 
which contains a method, next that is responsible for returning 
the moving average from a stream of integers.
Note: a moving average is the average of a subset of data at a given point in time.

Ex: Given the following series of events...

// i.e. the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4 
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
"""
from collections import deque

class MovingAverage:
  # Space: O(n)
  # Time: next -> O(1)
  def __init__(self, sizeValue):
    self.size = sizeValue
    self.queue = deque()
    self.queueSum = 0
  
  def next(self, val):
    if len(self.queue) == self.size:
      first = self.queue.popleft()
      self.queueSum -= first

    self.queueSum += val
    self.queue.append(val)

    return self.queueSum//len(self.queue)



mv = MovingAverage(3)

assert mv.next(3) == 3
assert mv.next(5) == 4
assert mv.next(7) == 5
assert mv.next(6) == 6

print("Passed all tests!")

