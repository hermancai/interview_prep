"""
53: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.


Solutions: 

##### 1
Loop through list, using first value as initial final and current max sum.
Update current max to previous current max or previous current max + current val.
Update final max to previous final max or current max.

Time: O(n)
Space: O(1)

"""

def maxSubarray(nums: list) -> int:
  currSum = maxSum = nums[0]

  for i in range(1, len(nums)):
    # Can the current value increase the current sum?
    # If the current value is larger than adding the current sum, 
    # the current running sum is now using a new subarray starting at the current value.
    # Otherwise the current value will join the existing subarray.
    currSum = max(nums[i], currSum + nums[i])

    # Did the new currSum beat the final answer?
    maxSum = max(maxSum, currSum)

  return maxSum


if __name__ == "__main__":
  print(maxSubarray([1, -2, 5]))
