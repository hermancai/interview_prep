"""
207: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Solutions:

##### 1 (own solution, very inefficient)
Use map. Key = course number; Value = set of prereqs
Loop through prerequisites:
  Add course1 to map.
  Loop through map:
    If course1 exists as prereq to other courses in map:
      Add course1 as prereq to curr course
  If prereq1 is already in map:
    Add all prereqs of prereq1 to course1 prereqs
Loop through map:
  Loop through prereqs of curr course:
    If prereq is in map and curr course is a prereq to curr prereq:
      Return False
Return True

Time: O(I don't want to think about it)


##### 2
Kahn's algorithm:
The given list can be represented as a DAG (Directed Acyclic Graph).
Create adjacency list.
Create inDegree list (number of incoming edges) for each node.
Keep counter of visited nodes, initially 0.
Get all nodes with 0 indegree and add to queue.
While queue is not empty:
  Increment visited counter
  Decrement indegree of all neighbor nodes
    If indegree of neighbor node is now 0, add to queue
If visited counter is not equal to number of nodes, topological sort is not possible.

Time: O(V + E)
Space: O(V)

"""
from collections import deque

# Solution 1
def canFinish1(numCourses: int, prerequisites: list[list[int]]) -> bool:
  m = {}
  for course, prereq in prerequisites:
    if course not in m:
      m[course] = set([prereq])
    else:
      m[course].add(prereq)
        
    for c in m.keys():
      if course in m[c]:
        m[c].add(prereq)
        
    if prereq in m:
      for c in m[prereq]:
        m[course].add(c)
          
  for course in m.keys():
    for prereq in m[course]:
      if prereq in m and course in m[prereq]:
        return False
        
  return True


# Solution 2
def canFinish2(numCourses: int, prerequisites: list[list[int]]) -> bool:
  # adjList: each prereq (index) points to a list of courses that depend on it aka outgoing edges
  # inDegrees: number of incoming edges to each course (index)
  adjList = [[] for _ in range(numCourses)]
  inDegrees = [0 for _ in range(numCourses)]
  for req, course in prerequisites:
    adjList[course].append(req)
    inDegrees[req] += 1

  # Add all nodes with no incoming edges to queue
  q = deque()
  for i in range(numCourses):
    if inDegrees[i] == 0:
      q.append(i)

  # Loop until empty queue
  visited = 0
  while q:
    node = q.popleft()
    visited += 1
    # Remove incoming edge from current node to neighbor nodes
    for prereq in adjList[node]:
      inDegrees[prereq] -= 1
      # When a node has no more incoming edges, it becomes independent
      if inDegrees[prereq] == 0:
        q.append(prereq)
  
  # Every node should have been visited if valid
  return visited == numCourses

if __name__ == "__main__":
  print(canFinish2(4, [[0, 1],[2, 3],[1, 2],[3, 0]]))
