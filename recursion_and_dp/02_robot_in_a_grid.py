'''
There is a robot at the top left corner of a grid of r rows and c columns. 
The robot can only move left and right onto valid grid cells. 
Find a path from the top left corner to the bottom right corner.

Solution:

Use a list to keep track of the path and a set to track visited cells.
Start from the bottom right corner: (r, c).
Base case:
  If the adjacent cell is out of bounds or invalid: return false.

If the cell has been visited: return false.  
If the cell is the top left corner OR
  recursive call to right cell returns true OR 
  recursive call to top cell returns true:
    Add current cell to the path.
    NOTE: Nothing gets added to the final path until the recursive calls 
          reach the top left corner. 
    Return true.
Else add the cell to visited and return false.

Time: O(r * c)
Space: O(r * c)

'''


class Point:
  def __init__(self, row, col):
    self.row, self.col = row, col

  def __repr__(self):
    return "(" + str(self.row) + ", " + str(self.col) + ")"

  def __hash__(self):
    return hash((self.row, self.col))

  def __eq__(self, other):
    if not isinstance(other, type(self)): return NotImplemented
    return other.col == self.col and other.row == self.row


def getPath(grid):
  path = []
  visited = set()
  helper(grid, path, visited, len(grid) - 1, len(grid[0]) - 1)
  return path if path else None

def helper(grid, path, visited, row, col):
  if row < 0 or col < 0 or not grid[row][col]: return False

  p = Point(row, col)
  if p in visited: return False

  if (row == 0 and col == 0) or \
    helper(grid, path, visited, row - 1, col) or \
    helper(grid, path, visited, row, col - 1):
      path.append(p)
      return True

  visited.add(p)
  return False


if __name__ == "__main__":
  grid = [
    [True,  False, False, False],
    [True,  True,  True,  False],
    [False, False, True,  False],
    [False, False, True,  True],
    [False, False, False, True]
  ]

  print(getPath(grid))
