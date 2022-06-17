"""
121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to 
buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Input:  [7, 1, 5, 3, 6, 4]
Output: 5


Solutions: 

##### 1
Keep track of minimum price and maximum profit. 
Loop through list, updating both values. Return max profit.

Time: O(n)
Space: O(1)

##### 2
Use two pointers to loop through list. Keep track of max.
While right pointer is less than list length:
  If left value is less than right value, can profit:
    Update max
  Else: Set left pointer equal to right pointer
  Increment right pointer

"""

# Solution 1
def getMaxProfit(prices: list) -> int:
  maxProfit, minPrice = 0, float("inf")

  for v in prices:
    minPrice = min(minPrice, v)
    maxProfit = max(maxProfit, v - minPrice)

  return maxProfit


# Solution 2
def maxProfit(prices: list) -> int:
  l, r = 0, 1
  maxP = 0

  while r < len(prices):
    # If a profit can be made
    if prices[l] < prices[r]:
      maxP = max(maxP, prices[r] - prices[l])
    else:
      # If profit was made, r is always higher value than current l.
      # Now r is lower than l (i.e. no profit) so set current r to l as new min value
      l = r
    r += 1

  return maxP


if __name__ == "__main__":
  print(maxProfit([7, 1, 5, 3, 6, 4]))
