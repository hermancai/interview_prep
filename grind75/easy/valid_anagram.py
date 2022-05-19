"""
242: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Solutions:

##### 1
Compare string lengths. Return false if not equal
Create frequency map of one string.
For each char in other string, decrement the count.
  If char not in map or count less than 0, return false.

Time: O(n)
Space: O(n)

"""

def isAnagram(s: str, t: str) -> bool:
  if len(s) != len(t): return False

  m = {}
  for c in s:
    if c in m: m[c] += 1
    else: m[c] = 1

  for c in t:
    if c not in m: return False
    m[c] -= 1
    if m[c] < 0: return False

  return True


if __name__ == "__main__":
  print(isAnagram("anagram", "gnaamra"))
