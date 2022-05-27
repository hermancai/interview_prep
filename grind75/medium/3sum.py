"""
15: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Solutions: 

##### 1
Create 2 sets holding positive and negative values. Keep count of 0s.
If at least one 0:
  Loop through one set and look for complement in other set.
  Add to results if found.
If at least 3 0s: add [0, 0, 0] to results.
Nested loop through positive set to add all pairs:
  If complement exists in negative: add to results.
Do same nested loop for negative set.

Time: O(n ^ 2)
Space: O(n)


##### 2
Sort list.
Loop through list:
  If prev value is same as curr: continue
  Target is opposite sign of current value
  Use two pointers: left = curr + 1, right = len(nums) - 1
  While left is less than right:
    If left + right elements equals target: 
      Add to results
      Increment left until pointing to last dupe of current left value
      Decrement right until pointing to first dupe of current right value
      Increment left once and decrement right once (now both point to new value)
    Else if target is bigger than left + right sum:
      Increment left
    Else target is less than left + right sum:
      Decrement right

Time: O(n ^ 2)
Space: O(n)

"""

# Solution 2
def getTriplets(nums: list) -> list:
  nums.sort()
  res = []

  for i in range(len(nums)):
    # If current value is same as previous
    if i > 0 and nums[i] == nums[i - 1]: continue

    target = -nums[i]
    l, r = i + 1, len(nums) - 1
    while l < r:
      twoSum = nums[l] + nums[r]
      if twoSum == target:
        res.append([nums[i], nums[l], nums[r]])
        # Skip dupes from left and right pointers
        while l < r and nums[l] == nums[l + 1]: l += 1
        while l < r and nums[r] == nums[r - 1]: r -= 1
        
        # Get next new values
        l += 1
        r -= 1
      elif twoSum < target:
        l += 1
      else:
        r -= 1
  return res


if __name__ == "__main__":
  print(getTriplets([-1,0,1,2,-1,-4]))
