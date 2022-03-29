"""
This question is asked by Amazon. Given a string s consisting of
only letters and digits, where we are allowed to transform any 
letter to uppercase or lowercase, return a list containing all 
possible permutations of the string.

Ex: Given the following string…

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""

from typing import List

def generatePermutations(string: str, currPos: int, output: List[str]) -> None:
  if currPos == len(string):
    output.append("".join(string))
    return
  
  if string[currPos].isalpha():
    string[currPos] = string[currPos].lower()
    generatePermutations([x for x in string], currPos+1, output)

    string[currPos] = string[currPos].upper()
    generatePermutations([x for x in string], currPos+1, output)

  else:
    generatePermutations([x for x in string], currPos+1, output)



def stringPermutations(string: str) -> List[str]:
  # Time O(2^n)
  # Space O(2^n)
  if len(string) == 0: return []

  output = []
  string = [c for c in string]

  generatePermutations(string, 0, output)
  return output


assert stringPermutations("c7w2") == ["c7w2", "c7W2", "C7w2", "C7W2"]

print("Passed all tests!")