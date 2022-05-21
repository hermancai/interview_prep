'''
Given an NxN matrix, rotate the matrix 90 degrees in place.

Input:
 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15  16

Output:
13   9   5   1
14  10   6   2
15  11   7   3
16  12   8   4

Notes:
0, 0    0, 1    0, 2    0, 3
1, 0    1, 1    1, 2    1, 3
2, 0    2, 1    2, 2    2, 3
3, 0    3, 1    3, 2    3, 3

3, 0    2, 0    1, 0    0, 0
3, 1    2, 1    1, 1    0, 1
3, 2    2, 2    1, 2    0, 2
3, 3    2, 3    1, 3    0, 3

Solution:
Swap values for each layer and work inwards.

Time: O(n^2)
Space: O(1)

'''

def rotateMatrix(li: list):
  n = len(li)
  layer = 0

  # Loop through layers
  while layer < n / 2:
    # Track stop and start indices for one side of current layer
    first = layer
    last = n - 1 - layer

    # Loop through side of current layer
    for i in range(first, last):
      offset = i - first
      top = li[first][i]  # Save value for later

      li[first][i] = li[last - offset][first]  # Replace top with left
      li[last - offset][first] = li[last][last - offset]  # Replace left with bottom
      li[last][last - offset] = li[i][last]  # Replace bottom with right
      li[i][last] = top  # Replace right with top
    
    layer += 1

  return li


if __name__ == "__main__":
  li = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
  ]
  rotateMatrix(li)

  for l in li:
    print(l)