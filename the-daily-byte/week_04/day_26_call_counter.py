"""
This question is asked by Google. Create a class CallCounter that 
tracks the number of calls a client has made within the last 3 seconds. 
Your class should contain one method, ping(int t) that receives the current 
timestamp (in milliseconds) of a new call being made and returns the number 
of calls made within the last 3 seconds.
Note: you may assume that the time associated with each subsequent call to 
ping is strictly increasing.

Ex: Given the following calls to ping…

ping(1), return 1 (1 call within the last 3 seconds)
ping(300), return 2 (2 calls within the last 3 seconds)
ping(3000), return 3 (3 calls within the last 3 seconds)
ping(3002), return 3 (3 calls within the last 3 seconds)
ping(7000), return 1 (1 call within the last 3 seconds)
"""

from collections import deque

class CallCounter:
  # Time: O(N) where N is the number of queries made to ping.
  # Space: generally speaking O(W) where W is our window size 
  # but this can be considered O(1) in our case since our window size is fixed at 3 seconds.
  def __init__(self):
    self.queue = deque()
  
  def ping(self, t):
    self.queue.append(t)

    while len(self.queue) != 0 and self.queue[0] < t - 3000:
      self.queue.popleft()

    return len(self.queue)
      

obj = CallCounter()

assert obj.ping(1) == 1
assert obj.ping(300) == 2
assert obj.ping(3000) == 3
assert obj.ping(3002) == 3
assert obj.ping(7000) == 1

print("Passed all tests!")