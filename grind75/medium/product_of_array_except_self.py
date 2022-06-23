"""
238: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Solutions:

##### 1
Create answer list of equal length with initial value = 1.
Loop through nums starting with multiplier = 1:
  Put multiplier * num in answer[i]
  Update multipler to include current num
Loop backwards through nums with same operations as above

Time: O(n)
Space: O(n)

"""

def productArray(nums: list[int]) -> list[int]:
  n = len(nums)
  res = [1 for _ in range(n)]

  left = 1
  for i in range(n):
    res[i] *= left
    left *= nums[i]

  right = 1
  for i in range(n - 1, -1, -1):
    res[i] *= right
    right *= nums[i]
  
  return res


if __name__ == "__main__":
  print(productArray([1, 2, 3, 4]))
