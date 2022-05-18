"""
125: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.


Solutions: 

##### 1
Use two pointers, start and end, to loop through string. 
When incrementing pointers, skip non-alphanumeric chars.

Time: O(n)
Space: O(1)

"""

def isPalindrome(s: str) -> bool:
  start, end = 0, len(s) - 1

  while start < end:
    if not s[start].isalnum():
      start += 1
    elif not s[end].isalnum():
      end -= 1
    else:
      if s[start].lower() != s[end].lower():
        return False
      start += 1
      end -= 1

  return True


if __name__ == "__main__":
  print(isPalindrome("A man, a plan, a canal: Panama"))
