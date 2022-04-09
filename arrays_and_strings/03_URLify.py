'''
Replace all spaces in a string with '%20'.
There is space at the end of the string to hold the extra chars.
You are also given the true length of the string.

Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Solution: 

Turn string into list of chars for space efficiency.
Loop through string backwards, starting at true length index.
Check and replace chars starting at last index.
Return joined list of chars.

Time: O(n)
Space: O(1)

'''

def replaceSpaces(s: str, i: int):
  s = [x for x in s]  # Split string into char list

  oldI = i - 1  # True index
  newI = len(s) - 1

  # Loop backwards through string, replacing chars
  while oldI >= 0 and newI >= 0:
    if s[oldI] == " ":
      s[newI] = "0"
      s[newI - 1] = "2"
      s[newI - 2] = "%"
      newI -= 3
    else:
      s[newI] = s[oldI]
      newI -= 1
    oldI -= 1

  return "".join(s)

if __name__ == "__main__":
  s = "Mr John Smith    "
  print(replaceSpaces(s, 13))
