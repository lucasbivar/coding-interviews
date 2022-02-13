"""
This question is asked by Facebook. Given a string and the 
ability to delete at most one character, return whether or
not it can form a palindrome.

Note: a palindrome is a sequence of characters that reads the 
same forwards and backwards.
"""

def isPalindrome(string: str, begin: int, end: int) -> bool:
  while begin < end:
    if string[begin] != string[end]: return False

    begin += 1
    end -= 1
  
  return True

def validPalindrome(string: str) -> bool:
  # Time: O(n)
  # Space: O(1)
  begin = 0
  end = len(string)-1

  while begin < end:
    if string[begin] != string[end]:
      return isPalindrome(string, begin+1, end) or isPalindrome(string, begin, end-1)

    begin += 1
    end -= 1
  
  return True


assert validPalindrome("abcba") == True
assert validPalindrome("foobof") == True
assert validPalindrome("abccab") == False

print("Passed all tests!")