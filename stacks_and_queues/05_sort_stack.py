'''
Sort a stack to have smallest items on top.
One temporary stack is allowed but no other data structures.

Input:  [4, 3, 7, 8, 5, 2, 1]
Output: [8, 7, 5, 4, 3, 2, 1]

Solution:
Given unsorted stack s1 and temp descending sorted stack s2.
While s1 has elements:
  Push s1 to s2 while s1 peek is greater than s2 peek.
  If s1 peek is greater:
    Pop s1 into temp variable
    Pop s2 to s1 until s2 peek is less than temp var
    Push temp var to s2
Push all of sorted s2 back into empty s1.

Time: O(n^2)
Space: O(n)

'''

def sort(s):
  s2 = []

  while s:
    temp = s.pop()
    while s2 and s2[-1] > temp:
      s.append(s2.pop())
    s2.append(temp)

  while s2:
    s.append(s2.pop())


if __name__ == "__main__":
  s = [4, 3, 7, 8, 5, 2, 1]
  sort(s)
  print(s)
