"""
169: https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.


Solutions:

##### 1
Use a map to count element frequency. 
If the count of the current element is more than (n // 2): return element.

Time: O(n)
Space: O(n)

##### 2 
Fancy algorithm found in leetcode discussions:
Initialize variables count = 1 and major = nums[0]
Increment/decrement while looping through rest of list.
  If the count is 0: increment and update major = nums[n].
  If nums[n] == major: increment count.
  Else count is more than 0 but current val is not major: decrement count.
Return major.

This algorithm only works because it is guaranteed that a solution exists.
More than half of the list will be the same int.
The values cancel each other out by setting the count to 0.
At the end the list, major will hold the answer.

Time: O(n)
Space: O(1)

"""

def majority(nums: list) -> int:
  m = {}
  maj = len(nums) // 2

  for val in nums:
    if val not in m:
      m[val] = 1
    else:
      m[val] += 1
      if m[val] > maj:
        return val

def majority2(nums: list) -> int:
  major = nums[0]
  count = 1

  for i in range(1, len(nums)):
    # Every previous value has been canceled out so there is no current major.
    if count == 0:
      count += 1
      major = nums[i]
    # Increment count for current major.
    elif major == nums[i]:
      count += 1
    # Current val is not major but previous values have not been canceled out.
    else:
      count -= 1
  return major

  
if __name__ == "__main__":
  print(majority2([2, 2, 1, 1, 1, 2, 2]))
