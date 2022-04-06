'''
Determine if all characters in a string are unique. 
What if you can't use extra data structures?

Ask:
Is the string ASCII or Unicode?

If the format has 128 unique characters, a string with more than 128
characters cannot be unique.

Solutions:
### 1
Assume: ASCII (128 unique chars)

Return false if length of string is greater than 128.
Use a fixed array of booleans filled with false.
Loop through string and mark index of character in array to true.
If bool at index is already true, return false.
Return true.

Time: O(n) or O(1) because loop iterates at most a fixed count. 
Space: O(1) because fixed char set size.

### 2
Assume: Character set is not fixed.

Create empty map. 
Loop through string, adding each char to map.
If char is already in map, return false.
Return true.

Time: O(mind(c, n)) where c is size of char set.
Space: O(c) where c is size of char set.
'''