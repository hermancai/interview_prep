"""
542: https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.


Solutions:

##### 1
Use a queue to do breadth first traversal. Queue stores tuple of row and index
Loop through matrix:
  If cell is 0: Append to queue.
  Else: set cell to -1 (not visited).
While q is not empty:
  Pop from queue. 
  Get adjacent 4 cells based on current indices.
  If adjacent cell is not valid or already visited: continue
  Else:
    Set new cell value to current value + 1
    Append new cell to queue
Return matrix

Time: O(m * n)
Space: O(1)

"""

from collections import deque

def updateMatrix(mat):
  q = deque()
  r, c = len(mat), len(mat[0])

  # Set entire matrix to -1 for unvisited except for 0s. Add '0' cells to queue
  for row in range(r):
    for col in range(c):
      if mat[row][col] == 0:
        q.append((row, col))
      else:
        mat[row][col] = -1

  # Increments of current row and col to get 4 adjacent cells
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

  # Breadth first traversal adding adjacent cells
  # If current cell is X spaces from a 0 cell, 
  # then adjacent cells are X + 1 spaces away !! if unvisited !!
  while q:
    currR, currC = q.popleft()
    for i in range(len(directions)):
      newR, newC = currR + directions[i][0], currC + directions[i][1]
      if newR >= c or newR < 0 or newC >= c or newC < 0 or mat[newR][newC] != -1:
        continue
      mat[newR][newC] = mat[currR][currC] + 1
      q.append((newR, newC))
  
  return mat


if __name__ == "__main__":
  print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
