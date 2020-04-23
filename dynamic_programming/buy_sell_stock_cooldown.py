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
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        sell = [0] * len(prices)
        buy = [0] * len(prices)

        # base case
        sell[0] = 0
        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            # buy 1 day before, sell today
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

            # best buy price if we sell two days ago
            sell_two_days_ago = sell[i - 2] if i > 1 else 0
            buy[i] = max(buy[i - 1], sell_two_days_ago - prices[i])

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
