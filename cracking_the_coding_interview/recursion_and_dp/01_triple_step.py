'''
You can run up a staircase with n steps and can hop either 1 step, 
2 steps, or 3 steps at a time. How many possible ways can you run up the steps?

Solution:

Use memoization with recursion. 
Starting with n steps, find the number of ways for (n-1), (n-2), and (n-3).
If the answer is already in the memo, return that answer.
Else store the answer in the memo and return the answer.
Base cases:
  If n is less than 0: 
    The call is invalid because the subtracted steps is more than steps left.
    Return 0
  If n is 0:
    No more steps can be made. Return 1 to account for last call.

Time: O(n)
Space: O(n)

NOTE: The number result can overflow quickly, depending on the language.

'''

def getSteps(n: int) -> int:
  memo = [-1] * (n + 1)
  return helper(n, memo)

def helper(n: int, memo: list) -> int:
  if n < 0: return 0
  if n == 0: return 1
  if memo[n] > -1: return memo[n]

  memo[n] = helper(n - 1, memo) + helper(n - 2, memo) + helper(n - 3, memo)
  return memo[n]


if __name__ == "__main__":
  print(getSteps(10))
