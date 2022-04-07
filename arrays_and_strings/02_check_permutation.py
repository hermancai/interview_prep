'''
Given two strings, decide if one is a permutation of the other.

Ask:
Case sensitive? Does whitespace matter?

Solutions:

##### 1
Given: No whitespace, not case sensitive

Return false if not equal string lengths.
Sort strings and compare.

Time: O(n log n)
Space: Depends on sorting algorithm


##### 2
Given: No whitespace, not case sensitive

Return false if not equal string lengths.
Create a char frequency map for the first string.
Loop through second string
  Decrement count for each char
  Return false if count is negative

Time: O(n)
Space: O(n)

'''

# Solution 2
def checkPermutation(s1: str, s2: str) -> bool:
  m = {}
  for c in s1:  # Loop through first string
    m[c] = m.get(c, 0) + 1  # Increment count or initialize

  for c in s2:  # Loop through second string
    if c not in m:
      return False
    
    m[c] -= 1
    if m[c] < 0:
      return False

  return True


if __name__ == "__main__":
  s1 = "asdf"
  s2 = "fasd"
  print(checkPermutation(s1, s2))
