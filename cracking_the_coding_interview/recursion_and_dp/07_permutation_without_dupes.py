'''
Create all permutations of a string of unique characters.

Solutions: 

##### 1
Cases:
a1:     a1
a1a2:   a2a1, a1a2,
a1a2a3: a3a2a1, a2a3a1, a2a1a3, a3a1a2, a1a3a2, a1a2a3

Recursively get to an empty string.
Going up the call stack, insert the new char between every index of 
the current string. 

Time: O(n * n!)
  There are n! permutations and n layers of recursion. 
Space: O(n * n!) for generating the strings.

'''

def getPerms(s: str) -> list:
  if s is None: return None  # Error check
  if len(s) == 0: return [""]  # Base case

  first, remainder = s[0], s[1:]
  words = getPerms(remainder)
  
  # Insert new char into every index of every old permutation
  permutations = []
  for word in words:
    for i in range(len(word) + 1):
      permutations.append(word[:i] + first + word[i:])

  print(permutations, end="\n\n")
  return permutations

if __name__ == "__main__":
  s = "asdf"
  print(getPerms(s))
