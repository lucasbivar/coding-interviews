"""
This question is asked by Amazon. Given a string representing your
stones and another string representing a list of jewels, return 
the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

def countJewels(jewels: str, stones: str) -> int:
  # Time: O(n+m)
  # Space: O(n)
  jewels = set(jewels)
  count = 0

  for stone in stones:
    if stone in jewels:
      count += 1
  
  return count 


assert countJewels("abc", "ac") == 2
assert countJewels("Af", "AaaddfFf") == 3
assert countJewels("AYOPD", "ayopd") == 0

print("Passed all tests!")