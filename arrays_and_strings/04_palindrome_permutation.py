'''
Decide if a string is the permutation of a palindrome.
Assume only alphabet and spaces, not case sensitive.

Input: "Tact Coa"
Output: True ("taco cat", "atco cta", etc)

Note:
Property of a palindrome: it can have at most one odd count of a character

Solution:

Create list of size 26 to track char frequency.
Loop through list.
  Return false if more than one odd count.
Return True.

Time: O(n)
Space: O(1)

'''

def palindromePermutation(s: str):
  s = s.lower()
  frequencyList = [0] * 26
  offset = ord("a")

  # Build frequency list
  for c in s:
    if not c.isalpha():
      continue
    frequencyList[ord(c) - offset] += 1

  # Check for more than one odd count in frequency list
  foundOdd = False
  for val in frequencyList:
    if val % 2 != 0:
      if foundOdd:
        return False
      foundOdd = True

  return True


if __name__ == "__main__":
  s = "Tact Coa"
  print(palindromePermutation(s))
