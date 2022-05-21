"""
278: https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.


Solutions:

##### 1
Binary search while keeping track of first bad version. 
Don't stop search until start > end.

Time: O(log n)
Space: O(1)

"""

# Hidden on leetcode
def isBadVersion(n: int) -> bool:
  pass

def findFirstBad(n: int) -> int:
  start, end = 0, n
  firstBad = None

  while start <= end:
    mid = (start + end) // 2
    if isBadVersion(mid):
      firstBad = mid
      end = mid - 1
    else:
      start = mid + 1

  return firstBad
