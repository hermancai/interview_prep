"""
383: https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Solutions: 

##### 1
Create a frequency map of magazine.
For each char in randomNote, decrement map counter
  return false if char is not in map or counter less than 0

Time: O(n + m) where n and m are lengths of strings
Space: O(1) if there are only 26 chars and whitespace

"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
  m = {}
  for c in magazine:
    if c in m:
      m[c] += 1
    else:
      m[c] = 1

  for c in ransomNote:
    if c not in m:
      return False
    m[c] -= 1
    if m[c] < 0:
      return False

  return True


if __name__ == "__main__":
  print(canConstruct("abc", "rueajhzxiackjjoijb"))
