"""
70: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?


Solutions: 

##### 1
Dynamic programming. 
To get the number of ways for n steps, find the ways for n-1 and n-2 steps.
Example: Find n = 4 steps.
n = 2 has ways: (1, 1), (2)
n = 3 has ways: (1, 1, 1), (2, 1), (1, 2)
n = 4 has ways: (1, 1, 2), (2, 2), (1, 1, 1, 1), (2, 1, 1), (1, 2, 1)
The solution for n = 4 is adding 2 to the solutions for n = 2, along with 
  adding 1 to the solutions for n = 3. 
A list of length n can be used to memoize previous answers.
Since only the previous two solutions are needed, the list can just be two variables.

Time: O(n)
Space: O(1)

"""

def getWays(n: int) -> int:
  if n >= 0 and n <= 2: return n

  # Starting with base cases n = 1 and n = 2
  twoBefore = 1
  oneBefore = 2

  for _ in range(3, n + 1):
    temp = twoBefore + oneBefore
    twoBefore = oneBefore
    oneBefore = temp

  return temp


if __name__ == "__main__":
  print(getWays(30))
