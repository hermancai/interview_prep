'''
You are given a function isSubstring() which checks if a word is a substring
of another word. 
Given strings s1 and s2, check if s2 is a rotation of s1
while only using one call to isSubstring().

Input: waterbottle, erbottlewat
Output: True

Solution:
If s2 is a rotation of s1, s2 will always be in s1s1

Time: O(n) for checking contain
Space: O(n) for doubling s1

'''

def isSubstring(s1: str, s2: str) -> bool:
  return s2 in s1

def isRotation(s1: str, s2: str) -> bool:
  if not s1 or not s2 or len(s1) != len(s2): return False
  return isSubstring(s1 * 2, s2)


if __name__ == "__main__":
  s1 = "waterbottle"
  s2 = "erbottlewat"
  print(isRotation(s1, s2))
