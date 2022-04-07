'''
Determine if all characters in a string are unique. 
What if you can't use extra data structures?

Ask:
Is the string ASCII or Unicode?

If the format has 128 unique characters, a string with more than 128
characters cannot be unique.

Solutions:

##### 1
Given: ASCII (128 unique chars)

Return false if length of string is greater than 128.
Use a fixed array of booleans filled with false.
Loop through string and mark index of character in array to true.
If bool at index is already true, return false.
Return true.

Time: O(n) or O(1) because loop iterates at most a fixed count
Space: O(1) because fixed char set size


##### 2
Given: Character set is not fixed.

Create empty map. 
Loop through string, adding each char to map.
If char is already in map, return false.
Return true.

Time: O(n) 
Space: O(n)


##### 3
Given: No additional data structures.

Compare every char in the string to every other char.

Time: O(n^2)
Space: O(1)


##### 4
Given: No additional data structures.

Sort string, then check neighbor char of each char.

Time: O(n log n)
Space: Depends on sorting algorithm.

'''

# Solution 2
def isUnique(s: str) -> bool:
  m = {}
  for c in s:
    if c in m:
      return False
    m[c] = True
  return True


if __name__ == "__main__":
  s = "asdf"
  print(isUnique(s))
