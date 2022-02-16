"""
This question is asked by Facebook. Given two strings s and t 
return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""

def validAnagram(s: str, t: str) -> bool:
  # Time: O(n)
  # Space: O(1) -> independent of the size of both strings the 
  # hashmap's length will be in maximum of 26 (alphabet)
  if len(s) != len(t): return False
  
  countLetters = dict()
  for c in s:
    if c not in countLetters:
      countLetters[c] = 0
    
    countLetters[c] += 1
  
  for c in t:
    if c not in countLetters:
      return False
    
    countLetters[c] -= 1
    if countLetters[c] == 0:
      del countLetters[c]
  
  return True 
  

assert validAnagram("cat", "tac") == True
assert validAnagram("listen", "silent") == True
assert validAnagram("program", "function") == False

print("Passed all tests!")