"""
This question is asked by Google. Given a string of digits, 
return all possible text messages those digits could send.
Note: The mapping of digits to letters is as follows…

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""

from typing import List

def generateHelper(string: str, currPos: int, currState: List[chr], output: List[str], digitsMap: dict) -> None:
  if len(string) == currPos:
    output.append("".join(currState))
    return
  
  if string[currPos] in digitsMap:
    for c in digitsMap[string[currPos]]:
      generateHelper(string, currPos+1, currState + [c], output, digitsMap)

  

def generateTextMessages(string: str) -> List[str]:
  # Time: O(4^n)
  # Space: O(4^n)
  digitsMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  }

  if len(string) == 0: return []
   
  output = []
  generateHelper(string, 0, [], output, digitsMap)

  return output


assert generateTextMessages("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

print("Passed all tests!")