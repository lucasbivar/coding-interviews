"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

def findBiggestWord(words):
  # Time: O(n)
  # Space: O(m)
  biggestWord = words[0]
  for word in words:
    if len(word) > len(biggestWord):
      biggestWord = word
  
  return biggestWord

def longestCommonPrefix(words):
  # Time: O(m*n) -> m: biggest string, n: number of strings
  # Space: O(m+n)
  if len(words) == 0: return ""

  charsAtCurrIdx = set()
  biggestWord = findBiggestWord(words)

  output = []
  for i in range(len(biggestWord)):
    found = False
    for j in range(len(words)):
      if i < len(words[j]):
        charsAtCurrIdx.add(words[j][i])
      else:
        found = True
        break

    if len(charsAtCurrIdx) != 1 or found:
      break
    else:
      output.append(biggestWord[i])

    charsAtCurrIdx.clear()

  return "".join(output)


assert longestCommonPrefix(["colorado", "color", "cold"]) == "col"
assert longestCommonPrefix(["a", "b", "c"]) == ""
assert longestCommonPrefix(["spot", "spotty", "spotted"]) == "spot"
assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

print("Passed all tests!")

