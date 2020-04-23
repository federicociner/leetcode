"""A robot is located at the top-left corner of a m x n grid (marked 'Start'
in the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

Example 1:

    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the
    bottom-right corner:
        1. Right -> Right -> Down
        2. Right -> Down -> Right
        3. Down -> Right -> Right

Example 2:

    Input: m = 7, n = 3
    Output: 28

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""


class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(n * m)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1

        for i in range(1, m):
            dp[0][i] = 1

        for j in range(1, n):
            dp[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    assert S.uniquePaths(3, 2) == 3

    # Example 2
    assert S.uniquePaths(7, 3) == 28

    print("All tests passed.")
