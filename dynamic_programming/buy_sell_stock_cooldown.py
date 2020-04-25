"""Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).

After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
day)

Example:

    Input: [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        sell = [0] * len(prices)
        buy = [0] * len(prices)

        # base cases
        sell[0] = 0
        sell[1] = max(0, prices[1] - prices[0])
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])

        for i in range(2, len(prices)):
            # sold yesterday and cool OR bought previous day and now selling
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

            # bought previously and hold or sold two days ago and buy now
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])

        return sell[-1]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    prices = [1, 2, 3, 0, 2]
    assert S.maxProfit(prices) == 3

    # Example 2
    prices = [1, 2, 3, 0, 2, 5, 7, 2, 0, 4]
    assert S.maxProfit(prices) == 12

    print("All tests passed.")
