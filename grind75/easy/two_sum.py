"""
1: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Solutions: 

##### 1
Brute force. For each number, loop through the list again to find complement.

Time: O(n^2)
Space: O(1)


##### 2
Create a map of the list. Key = number, Value = list of indices.
Loop through map to find complement.

Time: O(n)
Space: O(n)


##### 3:
Create a map of the list. While looping through the map, if the current 
number is not in the map, add its complement to the map instead. This only works 
because it is guaranteed that the list will have one solution. Eventually 
a complement will appear. Return a list of that complement and current index.

Time: O(n)
Space: O(n)

"""

# Solution 3
def twoSum(nums: list, target: int) -> list:
  m = {}
  for i in range(len(nums)):
    if nums[i] in m:
      return [i, m[nums[i]]]
    m[target - nums[i]] = i


if __name__ == "__main__":
  print(twoSum([2, 7, 11, 15], 22))
