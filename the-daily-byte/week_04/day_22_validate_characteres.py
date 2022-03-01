"""
This question is asked by Google. Given a string only containing the 
following characters (, ), {, }, [, and ] return whether or not the opening 
and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""

def validateCharacteres(string: str) -> bool:
  stack = []
  pairBrackets =  {"(": ")", "{": "}", "[":"]"}

  for c in string:
    if pairBrackets.get(c, None):
      stack.append(pairBrackets[c])
      
    else:
      if len(stack) == 0: return False
      top = stack.pop()
      if c != top: return False

  return True if len(stack) == 0 else False



assert validateCharacteres("(){}[]") == True

assert validateCharacteres("(({[]}))") == True

assert validateCharacteres("{(})") == False

print("Passed all tests!")