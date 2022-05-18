"""
20: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.


Solutions:

##### 1
Create dict of Key = opening paren, Value = closing paren
Use a stack. Loop through each char in string.
If the char is in the dict, push to stack.
Else the last element in stack must be the key of the current char.

Time: O(n)
Space: O(n)

"""

def validParen(s: str) -> bool:
  m = {"(": ")", "{": "}", "[": "]"}
  stack = []

  for char in s:
    if char in m:
      stack.append(char)
    else:
      if not stack or m[stack.pop()] != char:
        return False

  return len(stack) == 0


if __name__ == "__main__":
  print(validParen("{([][])}"))
