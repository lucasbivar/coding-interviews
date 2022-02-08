"""
This question is asked by Google. Given a string, reverse all of 
its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”

"""

def reverseString(str):
  # Time: O(n)
  # Space: O(n) [This happens cause we are converting an immutable string to a list. 
  # If we had received an array of char we could do it in a space complexity of O(1)]

  # strings in python are immutable, so we have to convert it to a list
  str = list(str)

  begin = 0
  end = len(str)-1

  while begin < end:
    str[begin], str[end] = str[end], str[begin]
    begin += 1
    end -= 1
  
  return "".join(str)

assert reverseString("Cat") == "taC"
assert reverseString("The Daily Byte") == "etyB yliaD ehT"
assert reverseString("civic") == "civic"

print("Passed all tests!")
