"""
322: https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Note that you cannot just start from the largest coin and decrement amount.
  The answer does not always include the largest coin.

Solutions:

##### 1
Dynamic programming. Bottom up idea: If list[i] has a solution, 
  it is 1 more coin than the previous valid solution at list[i - coin]
Create list of length = given amount + 1; all values set to infinity, list[0] = 0
Loop from 1 to amount, i = current amount you are trying to solve:
  Loop through coins:
    If current coin less than or equal to i:
      list[i] = min between infinity or value at list[i - coin] + 1
Return last value in list or -1

Time: O(n * amount) where n is length of coins list
Space: O(amount)

"""

def coinChange(coins: list[int], amount: int) -> int:
  memo = [0] + [float("inf") for _ in range(amount + 1)]

  for i in range(1, amount + 1):
    for coin in coins:
      # If current amount can fit current coin
      if i >= coin:
        # If [i - coin] had a valid answer, the answer of [i] is [i - coin] + 1
        # Note that memo[i] is not always inf
        memo[i] = min(memo[i], memo[i - coin] + 1)

  return -1 if memo[amount] == float("inf") else memo[amount]

if __name__ == "__main__":
  print(coinChange([1, 2, 5], 11))
