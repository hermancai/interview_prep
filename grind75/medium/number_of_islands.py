"""
200: https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Sample input:
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Solutions:

##### 1
Iterative breadth first traversal.
Keep track of total.
Nested loop through entire grid:
  If value is "1":
    Increment total.
    Perform BFT starting at current indices:
      Use new deque with starting indices as tuple.
      Loop until deque is empty:
        Pop from deque.
        Check 4 cardinal directions:
          Add to deque if valid indices and value is "1".
          Mark as visited "-1" to prevent re-adding
Return total.

Time: O(n * m)
Space: O(n * m)

"""

from collections import deque

def countIslands(grid: list[list[str]]) -> int:
  def markIsland(grid, row, col):
    q = deque()
    q.append((row, col))
    maxR, maxC = len(grid) - 1, len(grid[0]) - 1
    grid[row][col] = "-1"

    while q:
      curr = q.popleft()
      row, col = curr[0], curr[1]

      # Check top
      if row - 1 >= 0 and grid[row - 1][col] == "1":
        q.append((row - 1, col))
        grid[row - 1][col] = "-1"
                
      # Check bottom
      if row + 1 <= maxR and grid[row + 1][col] == "1":
        q.append((row + 1, col))
        grid[row + 1][col] = "-1"
      
      # Check right
      if col + 1 <= maxC and grid[row][col + 1] == "1":
        q.append((row, col + 1))
        grid[row][col + 1] = "-1"
      
      # Check left
      if col - 1 >= 0 and grid[row][col - 1] == "1":
        q.append((row, col - 1))
        grid[row][col - 1] = "-1"

  total = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "1":
            markIsland(grid, row, col)
            total += 1

  return total


if __name__ == "__main__":
  print(countIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
