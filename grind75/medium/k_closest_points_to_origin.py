"""
973: https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point 
on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).

NOTE:
Min heap is a binary tree where a node's children have lower values.
Can be represented as a list where the nth element (node) has its 
left and right child nodes at 2*n+1 and 2*n+2.
Deleting a node: 
  Replace the last leaf node value with the current node value. Delete leaf node.
  Move the newly placed leaf node value down the tree until correct position.
Inserting a node:
  Put value as new last node. Move node upwards in tree until correct position.
Both deleting and inserting take O(log n) where n is size of tree.

Solutions: 

##### 1
Use python builtin heap (min heap)* structure. 
We want to get rid of the highest value but min heap[0] is always the lowest value, 
  so simulate a max heap by flipping signs of distances.
Loop through every point:
  Calculate distance.
  If heap is full: push new value and pop head from heap
  Else: push new value.
Return heap as list.

Time: O(n log k) where n is number of given points and k is size of heap.
Space: O(k) where k is size of heap.

"""

import heapq

def getPoints(points: list, k: int) -> list:
  heap = []

  for x, y in points:
    distance = -(x * x + y * y)
    if len(heap) >= k:
      heapq.heappushpop(heap, (distance, x, y))
    else:
      heapq.heappush(heap, (distance, x, y))

  return [[x, y] for dist, x, y in heap]
