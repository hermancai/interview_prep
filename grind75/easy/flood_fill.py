"""
733: https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.
You are also given three integers sr, sc, and newColor. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color), and so on. Replace the color of all of the 
aforementioned pixels with newColor.
Return the modified image after performing the flood fill.


Solutions: 

##### 1
Use a queue and insert the initial spot. Check all 4 directions.
If the adjacent spot is valid and matches the initial value, 
add it to the queue. Repeat until the queue is empty.

Time: O(n)
Space: O(n)

"""

from collections import deque

def flood(image: list[list[int]], sr: int, sc: int, newColor: int):
  match = image[sr][sc]
  if match == newColor: return image

  q = deque()
  q.append((sr, sc))
  rowMax, columnMax = len(image) - 1, len(image[0]) - 1

  while q:
    curr = q.popleft()
    r, c = curr[0], curr[1]
    image[r][c] = newColor

    # check top
    if r - 1 >= 0 and image[r - 1][c] == match:
        q.append((r - 1, c))
    # check right
    if c + 1 <= columnMax and image[r][c + 1] == match:
        q.append((r, c + 1))
    # check bottom
    if r + 1 <= rowMax and image[r + 1][c] == match:
        q.append((r + 1, c))
    # check left
    if c - 1 >= 0 and image[r][c - 1] == match:
        q.append((r, c - 1))
    
  return image


if __name__ == "__main__":
  print(flood([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
