"""
This question is asked by Amazon. Given two strings s and t, 
which represents a sequence of keystrokes, where # denotes a 
backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""

def handleString(string: str) -> str:
  stack = []

  for c in string:
    if c == "#":
      if len(stack) == 0: continue
      stack.pop()
    else:
      stack.append(c)
  
  return "".join(stack)

def compareKeystrokes(str_s, str_t) -> bool:
  # Time: O(n + m)
  # Space: O(max(m+n))
  return handleString(str_s) == handleString(str_t)

assert compareKeystrokes("ABC#", "CD##AB") == True

assert compareKeystrokes("como#pur#ter", "computer") == True

assert compareKeystrokes("cof#dim#ng", "code") == False

print("Passed all tests!")