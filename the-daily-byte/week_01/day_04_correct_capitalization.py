"""
This question is asked by Google. Given a string, return whether or not it uses 
capitalization correctly. A string correctly uses capitalization if all letters are 
capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

def isUpperCase(char):
  #Time: O(1)
  #Space: O(1)
  if ord(char) >= 65 and ord(char) <= 90: 
    return True

  return False


def hasCorrectCapitalization(str):
  #Time: O(n)
  #Space: O(1)
  if len(str) <= 1: return True

  isFirstUpper = isUpperCase(str[0])
  hasUpperCase = False
  hasLowerCase = False

  for i in range(1, len(str)):
    if isUpperCase(str[i]):
      hasUpperCase = True
    else:
      hasLowerCase = True

  if isFirstUpper and not hasUpperCase and hasLowerCase: return True
  if isFirstUpper and hasUpperCase and not hasLowerCase: return True
  if not isFirstUpper and hasLowerCase and not hasUpperCase: return True

  return False

assert hasCorrectCapitalization("USA") == True
assert hasCorrectCapitalization("Calvin") == True
assert hasCorrectCapitalization("compUter") == False
assert hasCorrectCapitalization("engineerINg") == False
assert hasCorrectCapitalization("coding") == True

print("Passed all tests!")