"""
This question is asked by Apple. Given two binary strings 
(strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""
from collections import deque 

def addBinary(number1:str, number2: str) -> str:
  # Time: O(n) -> where "n" is the number of bits of the final sum
  # Space: O(n) or O(1) if we don't consider the output

  n1Pointer = len(number1)-1
  n2Pointer = len(number2)-1
  
  output = deque()
  carry = 0

  while n1Pointer >= 0 or n2Pointer >= 0:
    n1Digit = 0 if n1Pointer < 0 else int(number1[n1Pointer])
    n2Digit = 0 if n2Pointer < 0 else int(number2[n2Pointer])

    currDigitSum = n1Digit + n2Digit + carry
    carry = 1 if currDigitSum >= 2 else 0

    if currDigitSum == 2:
      currDigitSum = 0
    elif currDigitSum == 3:
      currDigitSum = 1

    output.appendleft(str(currDigitSum))
    n1Pointer -= 1
    n2Pointer -= 1

  if carry:
    output.appendleft(str(carry))
  
  return "".join(output)



assert addBinary("100", "1") == "101"
assert addBinary("11", "1") == "100"
assert addBinary("1", "0") == "1"

print("Passed all testes!")