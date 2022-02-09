"""
This question is asked by Amazon. Given a string representing
the sequence of moves a robot vacuum makes, return whether or not 
it will return to its original position. The string will only 
contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

def checkIfReturnToInit(sequenceOfMoves) -> bool:
  # Time: O(n)
  # Space: O(1)
  posX = 0
  posY = 0

  for c in sequenceOfMoves:
    if c == "L":
      posX -= 1
    elif c == "R":
      posX += 1
    elif c == "U":
      posY += 1
    elif c == "D":
      posY -= 1
  
  return True if posX == 0 and posY == 0 else False


assert checkIfReturnToInit("LR") == True
assert checkIfReturnToInit("URURD") == False
assert checkIfReturnToInit("RUULLDRD") == True

print("Passed all tests!")
