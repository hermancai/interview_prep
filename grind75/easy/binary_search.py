"""
704: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.


Solutions:

##### 1
Use start and end pointers to go through list.
Get mid index of current start and end. If value at index is 
less than target, search right side of list. Else left side.

Time: O(log n)
Space: O(1)


##### 2
Recursive. Use a helper to pass start and end pointers.

Time: O(log n)
Space: O(log n) for call stack

"""

# Solution 1
def search(nums: list, target: int) -> int:
  start, end = 0, len(nums) - 1

  while start <= end:
    mid = (start + end) // 2
    if nums[mid] > target:
      end = mid - 1
    elif nums[mid] < target:
      start = mid + 1
    else:
      return mid
  return -1

# Solution 2
def searchRecursive(nums: list, target: int) -> int:
  return helper(0, len(nums) - 1, nums, target)

def helper(start: int, end: int, nums: list, target: int) -> int:
  if start > end: return -1

  mid = (start + end) // 2
  if nums[mid] > target:
    return helper(start, mid - 1, nums, target)
  elif nums[mid] < target:
    return helper(mid + 1, end, nums, target)
  else:
    return mid

if __name__ == "__main__":
  print(searchRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
