"""
This question is asked by Google. Given an array of integers, 
return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""

from typing import List

def twoSum(nums: List[int], target: int) -> bool:
  # Time: O(n)
  # Space: O(n)
  seen = set()

  for num in nums:
    if (target-num) in seen:
      return True

    seen.add(num)
  
  return False


assert twoSum([1, 3, 8, 2], 10) == True
assert twoSum([3, 9, 13, 7], 8) == False
assert twoSum([4, 2, 6, 5, 2], 4) == True

print("Passed all tests!")