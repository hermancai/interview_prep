'''
A string can be edited three ways: insert char, remove char, replace char.
Given two strings, check if one string is one/zero edits away from the other.

Input -> Output:
pale,   pales -> True
pale,   ple   -> True
pale,   bale  -> True
pale,   bae   -> False

Note:
Inserting and removing a char mean the same thing, just with reversed order.

Solutions:

##### 1:
The strings can only have length difference of 0 or +/- 1.
Return False if larger difference.
If length difference of 0, check for replaced char.
Else check for changed char.

Time: O(n) where n is length of shorter string
Space: O(1)

'''

# s1 and s2 are same length
def checkReplace(s1: str, s2: str) -> bool:
  foundOneChange = False
  for i in range(len(s1) - 1):
    if s1[i] != s2[i]:
      if foundOneChange:
        return False
      foundOneChange = True
  return True

# s1 has one more char than s2
def checkEdit(s1: str, s2: str) -> bool:
  i1, i2 = 0, 0
  foundOneChange = False

  while i1 < len(s1) and i2 < len(s2):
    if s1[i1] != s2[i2]:
      if foundOneChange:
        return False
      foundOneChange = True
      i1 += 1
    else:
      i1 += 1
      i2 += 1

  return True


def oneAway(s1: str, s2: str) -> bool:
  lengthDiff = len(s1) - len(s2)

  if lengthDiff == 0:
    return checkReplace(s1, s2)
  
  if lengthDiff == 1:
    return checkEdit(s1, s2)

  if lengthDiff == -1:
    return checkEdit(s2, s1)

  return False


if __name__ == "__main__":
  s1 = "pale"
  s2 = "bae"
  print(oneAway(s1, s2))
