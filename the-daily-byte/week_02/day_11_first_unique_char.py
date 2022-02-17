"""
This question is asked by Microsoft. Given a string, 
return the index of its first unique character. If 
a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""


def indexOfFirstUniqueChar(string: str) -> int:
  # Time: O(n)
  # Space: O(n) or O(1) because we have a few letters in the alphabet
  indexOfChar = dict()

  for i, v in enumerate(string):
    if v in indexOfChar:
      indexOfChar[v] = -1 # appears more than one time
    else:
      indexOfChar[v] = i

  for key in indexOfChar:
    if indexOfChar[key] != -1: 
      return indexOfChar[key]
  
  return -1

assert indexOfFirstUniqueChar("abcabd") == 2
assert indexOfFirstUniqueChar("thedailybyte") == 1
assert indexOfFirstUniqueChar("developer") == 0
assert indexOfFirstUniqueChar("abab") == -1

print("Passed all tests!")