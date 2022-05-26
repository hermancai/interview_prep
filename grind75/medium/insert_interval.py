"""
57: https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the 
ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.


Solutions: 

##### 1
Start with a new empty results list.
While there is no overlap looping through list:
  Append intervals to the results.
While there is overlap looping through list:
  Update newInterval start as min(newInterval start, curr interval start)
  Update newInterval end as max(newInterval end, curr interval end)
Append rest of intervals list, which does not overlap

Time: O(n)
Space: O(n)

"""

def insertInterval(intervals: list, newInterval: list) -> list:
  res, i = [], 0

  while i < len(intervals) and newInterval[0] > intervals[i][1]:
    res.append(intervals[i])
    i += 1

  while i < len(intervals) and newInterval[1] >= intervals[i][0]:
    newInterval[0] = min(newInterval[0], intervals[i][0])
    newInterval[1] = max(newInterval[1], intervals[i][1])
    i += 1

  res.append(newInterval)

  while i < len(intervals):
    res.append(intervals[i])
    i += 1
  
  return res


if __name__ == "__main__":
  print(insertInterval([[1,3],[6,9]], [2,5]))
