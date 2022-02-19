"""
This question is asked by Google. Given two integer arrays,
return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

from typing import List

def intersectionOfNumbers(nums1: List[int], nums2: List[int]) -> List[int]:
  # Time: O(n+m)
  # Space: O(n+m)
  nums1 = set(nums1)
  nums2 = set(nums2)

  return list(nums1.intersection(nums2))

assert intersectionOfNumbers([2, 4, 4, 2], [2, 4]) == [2, 4]
assert intersectionOfNumbers([1, 2, 3, 3], [3, 3]) == [3]
assert intersectionOfNumbers([2, 4, 6, 8], [1, 3, 5, 7]) == []

print("Passed all tests!")