'''
Compress a string using the counts of repeated chars.
Return the original string if the new string is not shorter.
Assume only upper or lower alpha chars (Aa - Zz)

Input: aabcccccaaa
Output: a2b1c5a3

Solution: 

Create empty list to hold chars.
Place first char in string and 1 in list.
Loop through rest of string.
  If char is same as previous, increment count in list.
  Else increment list index and add new char and count to list.
Check length of list. Return original or joined list

Time: O(n)
Space: O(n)

'''

def compress(s: str) -> str:
  liIndex, strIndex = 0, 1
  li = []
  li.append(s[0])
  li.append(1)

  while strIndex < len(s):
    if s[strIndex] == li[liIndex]:
      li[liIndex + 1] += 1
    else:
      li[liIndex + 1] = str(li[liIndex + 1])
      liIndex += 2
      li.append(s[strIndex])
      li.append(1)
    strIndex += 1
  
  if len(li) >= len(s):
    return s

  li[-1] = str(li[-1])
  return "".join(li)


if __name__ == "__main__":
  s = "aabcccccaaa"
  print(compress(s))
