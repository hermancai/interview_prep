'''
Given an MxN matrix, if an element in the matrix is 0,
set the entire row and column to 0.

Solutions:

##### 1:
Use two lists to keep track of rows and columns that should be 0'ed.
Loop through matrix to update both lists.
Update matrix based on indices in both lists.

Time: O(MN)
Space: O(N) where N is longer side of matrix


##### 2:
Check first column and row for 0s. Use two bools to track.
Loop through rest of matrix. 
  If row i has 0, set matrix[i][0] to 0.
  If column j has 0, set matrix[0][j] to 0.
Loop through first row and column, setting 0s.
Set first row or column to 0 if bool is true.

Time: O(MN)
Space: O(1)

'''

def zeroMatrix(li: list) -> list:
  firstRowZero, firstColumnZero = False, False

  # Check first row for 0s
  for i in range(len(li[0])):
    if li[0][i] == 0:
      firstRowZero = True
      break

  # Check first column for 0s
  for i in range(len(li)):
    if li[i][0] == 0:
      firstColumnZero = True
      break

  # Loop through rest of matrix
  for i in range(1, len(li[0])):
    for j in range(1, len(li)):
      # Set current index of first row and column to 0
      if li[j][i] == 0:
        li[0][i] = 0
        li[j][0] = 0

  # Nullify columns based on first row
  for i in range(1, len(li[0])):
    if li[0][i] == 0:
      for j in range(len(li)):
        li[j][i] = 0

  # Nullify rows based on first column
  for i in range(1, len(li)):
    if li[i][0] == 0:
      for j in range(len(li[0])):
        li[i][j] = 0

  # Set first row to 0 if needed
  if firstRowZero:
    for i in range(len(li[0])):
      li[0][i] = 0

  # Set first column to 0 if needed
  if firstColumnZero:
    for i in range(len(li)):
      li[i][0] = 0

  return li


if __name__ == "__main__":
  li = [
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
  ]

  zeroMatrix(li)
  for l in li: print(l)
