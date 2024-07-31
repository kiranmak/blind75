"""
2. Best Time to Buy and Sell Stock

You are given an array of prices where prices[i] is the price of a
given stock on an ith day.
You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.

7,1,5,3,6,4
index curr buy sell profit
0      2    2   2    0
1      1    1   2   -1
2      2    1   2    1
3      1    1  1     0    
4      0    1  0    -1
5      1    0  1    1
6      2
"""
from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = -sys.maxsize
        max_profit = 0

        for curr in prices[1:]:
            if (curr - buy) > profit:
                profit = curr - buy
            
            if (curr - buy) < 0:
                buy = curr
            print("curr", curr, "buy", buy, "profit", profit)

            if profit > max_profit:
                max_profit = profit

        return 0 if max_profit < 0 else max_profit

    

s = Solution()
prices = [[7,1,5,3,6,4]]
prices += [[7,6,4,3,1]]
prices += [[1]]
prices += [[2,1,2,1,0,1,2]]

for prs in prices:
    print(prs)
    ans = s.maxProfit(prs)
    print(ans)
