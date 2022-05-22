"""
217: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.


Solutions:

##### 1
Create a set.
Loop through list. If int is already in set, return true.

Time: O(n)
Space: O(n)

"""

def containsDuplicates(nums: list) -> bool:
  m = set()
  for n in nums:
    if n in m:
      return True
    m.add(n)
  return False
