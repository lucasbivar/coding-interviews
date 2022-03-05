"""
This question is asked by Facebook. Given a string s containing only 
lowercase letters, continuously remove adjacent characters that are 
the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
"""

def removeAdjacentChars(string:str) -> str:
  # Time: O(n)
  # Space: O(n)
  
  stack = []

  for c in string:
    if len(stack) != 0 and stack[-1] == c:
        stack.pop()
    else:
      stack.append(c)

  return "".join(stack)


assert removeAdjacentChars("abccba") == ""
assert removeAdjacentChars("foobar") == "fbar"
assert removeAdjacentChars("abccbefggfe") == "a"

print("Passed all tests!")