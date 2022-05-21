"""
409: https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Solutions:

##### 1
Use a hashtable. Keep track of a count = 0.
Loop through the string:
  If the char exists in the map:
    Increment count by 2 and delete the char from the map.
  Else:
    Char count = 1 in map.
If the map contains anything, the char count is odd. Add 1 to final.

Time: O(n)
Space: O(n)

"""

def longest(s: str) -> int:
  m = {}
  count = 0

  for c in s:
    if c in m:
      count += 2
      del m[c]
    else:
      m[c] = 1

  return count + 1 if m else count


if __name__ == "__main__":
  print(longest("abccccdd"))
