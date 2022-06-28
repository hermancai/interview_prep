"""
994: https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:
  0 representing an empty cell,
  1 representing a fresh orange, or
  2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to 
  a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell 
  has a fresh orange. If this is impossible, return -1.


Solutions:

##### 1 (my own)
Keep track of minutes and whether rot spread occured in current iteration.
Infinite loop:
  Nested loop through grid:
    If value is 2:
      Spread rot. Mark new rot with value 3
      Set rot spread to True
  If rot did not spread: 
    Break
  Increment minutes and reset rot spread to False
  Nested loop through grid to set all values of 3 to 2
Nested loop through grid:
  Return -1 if value of 1 is found.
Return minutes

Time: O(k * m * n) where k = max(m, n). K is max number of iterations of the infinite loop.
Space: O(1)


##### 2
https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)
Use a queue that holds rotten spots and track minutes.
Loop to get number of initial fresh spots. Also add all rotten spots to queue.
Loop while queue is not empty and there are still fresh spots:
  Increment minutes. 
  Loop for length of queue:
    Pop from queue.
    Spread in 4 directions:
      Check if spot is valid.
      Check that spot is not 0 or 2 (aka already visited)
      Decrement fresh and add new rotten spot to queue.
Return minutes or -1 if fresh count is not 0.
  
Time: O(m * n)
Space: O(m * n)

"""

# Solution 1
def orangesRotting(grid: list[list[int]]) -> int:
  def rot(grid, row, col):
    grid[row][col] = 0
    foundRot = False
    
    # Spread to adjacent spots
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nr, nc = row + dr, col + dc
      if nr < 0 or nr > len(grid) - 1 or nc < 0 or nc > len(grid[0]) - 1:
        continue
      if grid[nr][nc] == 0 or grid[nr][nc] == 3 or grid[nr][nc] == 2:
        continue
      grid[nr][nc] = 3
      foundRot = True
    
    return foundRot

  minutes = 0
  newRot = False

  while True:
    # Spread rot for current iteration
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 2:
          foundRot = rot(grid, row, col)
          if foundRot:
            newRot = True
    
    # Finish if no spread occurred this iteration
    if not newRot:
      break
    minutes += 1   
    newRot = False
    
    # Mark all new rotted spots for next iteration
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 3:
          grid[row][col] = 2

  # Check if any fresh still exists in grid
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == 1:
        return -1

  return minutes


if __name__ == "__main__":
  print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
