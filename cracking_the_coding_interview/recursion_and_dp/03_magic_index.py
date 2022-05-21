'''
A magic index in a list is an index such that list[i] == i. 
Given a sorted list of unique integers, find a magic index. 
What if the values are not unique?

Index:     0   1  2  3  4  5  6  7  8   9  10
Input:  [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]
Output: 2

Solutions:

##### 1
Assuming unique integers.

Binary search.
Get middle index of current range.
If i equals A[i], return i.
If i is greater than A[i], the magic index must be on the right side.
If i is less than A[i], the magic index must be on the left side. 

Time: O(log n)
Space: O(log n) if recursive. O(1) if iterative.


##### 2
Assuming not unique integers.

Binary search with dynamic ranges for start and end.
Get middle index of current range.
If i equals A[i], return i.
Since duplicates are allowed, comparing mid and A[mid] is not enough. 
Recursively check both left and right sides with dynamic boundaries:
  In example input, with current mid as A[5] = 3, the left side's boundary 
    cannot end at A[4] because the highest value A[4] can hold is 3. The 
    end would be the minimum between (mid - 1) and (A[mid]).
  Similarly for the right side, the start would be the max between (mid + 1) 
    and (A[mid])
'''

# Solution 1
def magicIndex1(li):
  return helper1(li, 0, len(li) - 1)

def helper1(li, start, end):
  if start > end: return None

  mid = (start + end) // 2
  if mid == li[mid]: return mid
  if mid > li[mid]: return helper1(li, mid + 1, end)
  if mid < li[mid]: return helper1(li, start, mid - 1)

# Solution 2
def magicIndex2(li):
  return helper2(li, 0, len(li) - 1)

def helper2(li, start, end):
  if start > end: return None

  mid = (start + end) // 2
  if mid == li[mid]: return mid

  left = helper2(li, start, min(mid - 1, li[mid]))
  if left is not None: return left

  right = helper2(li, max(mid + 1, li[mid]), end)
  # if right is not None: return right
  # return None
  
  # Above returns refactor into:
  return right


if __name__ == "__main__":
  li = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
  li2 = [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]
  # print(magicIndex1(li))  # This will fail for li2 as expected
  print(magicIndex2(li2))
