"""Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

Example 1:

    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3),
    profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1
    = 3.

Example 2:

    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
    profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as
    you are engaging multiple transactions at the same time. You must sell
    before buying again.

Example 3:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        n = len(prices)
        left_min = prices[0]
        right_max = prices[-1]

        left_profits = [0] * n
        right_profits = [0] * (n + 1)

        for l in range(1, n):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = n - l - 1
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0

        for i in range(n):
            max_profit = max(
                max_profit, left_profits[i] + right_profits[i + 1]
            )

        return max_profit


class SolutionOptimizedSpace:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        one_buy = two_buy = float("inf")
        one_profit = two_profit = 0

        for price in prices:
            one_buy = min(one_buy, price)
            one_profit = max(one_profit, price - one_buy)
            two_buy = min(two_buy, price - one_profit)
            two_profit = max(two_profit, price - two_buy)

        return two_profit


if __name__ == "__main__":
    S = Solution()

    # Example 1
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert S.maxProfit(prices) == 6

    # Example 2
    prices = [1, 2, 3, 4, 5]
    assert S.maxProfit(prices) == 4

    # Example 3
    prices = [7, 6, 4, 3, 1]
    assert S.maxProfit(prices) == 0
    print("All tests passed.")
