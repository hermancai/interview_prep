"""
3: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.


Solutions:

##### 1
Use two pointers to iterate through string.
Keep track of max length and use set to check for duplicate chars.
While pointers start and end are within boundaries:
  While s[end] is in set:
    Remove char from set. Increment start.
  Add s[end] to set.
  Update max length.
  Increment end.

Time: O(n)
Space: O(n)

"""

def getLongest(s: str) -> int:
  if not s: return 0

  charSet = set()
  start, end = 0, 0
  maxLength = 0

  while start < len(s) and end < len(s):
    # Increment start until current substring has no dupes
    while s[end] in charSet:
      charSet.remove(s[end])
      start += 1

    charSet.add(s[end])
    maxLength = max(maxLength, end - start)
    end += 1
  
  return maxLength + 1
