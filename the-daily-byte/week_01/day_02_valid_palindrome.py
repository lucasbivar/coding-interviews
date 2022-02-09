"""
This question is asked by Facebook. Given a string, return whether or not it forms a 
palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

def isAlphabetical(char) -> bool:
  if ord(char) >= 97 and ord(char) <= 122: return True

  return False


def validPalindrome(str) -> bool:
  # Time: O(n)
  # Space: O(1)

  begin = 0
  end = len(str)-1

  str = str.lower() # O(n)

  while begin < end:
    if isAlphabetical(str[begin]) and isAlphabetical(str[end]):
      if str[begin] != str[end]: return False

      begin += 1
      end -= 1
    
    if not isAlphabetical(str[begin]):
      begin += 1
    
    if not isAlphabetical(str[end]):
      end -= 1
  
  return True

assert validPalindrome("level") == True
assert validPalindrome("algorithm") == False
assert validPalindrome("A man, a plan, a canal: Panama.") == True

print("Passed all tests!")
