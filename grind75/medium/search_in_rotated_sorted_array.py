"""
33: https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Solutions:

##### 1
Get index of lowest value using binary search.
Perform binary search in updated range of indices, accounting for rotation.

Time: O(log n)
Space: O(1)

"""

def searchRotated(nums: list[int], target: int) -> int:
  def binarySearch(nums, target, start, end):
    while start <= end:
      mid = (start + end) // 2
      if nums[mid] == target:
        return mid
      if nums[mid] > target:
        end = mid - 1
      else:
        start = mid + 1
    return -1

  start, end = 0, len(nums) - 1
  while start < end:
    mid = (start + end) // 2
    if nums[mid] > nums[end]:
      start = mid + 1
    else:
      end = mid

  if target >= nums[start] and target <= nums[-1]:
    return binarySearch(nums, target, start, len(nums) - 1)
  return binarySearch(nums, target, 0, start - 1)


if __name__ == "__main__":
  print(searchRotated([4,5,6,7,0,1,2], 0))
