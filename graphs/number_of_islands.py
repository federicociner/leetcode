"""Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid \
are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1

Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3

"""
from typing import List


class Solution:
    # Time complexity: O(M * N)
    # Space complexity: O(M * N)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        num_islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(grid, i, j)

        return num_islands

    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        n = len(grid)
        m = len(grid[0])

        if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == "0":
            return

        grid[row][col] = "0"
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert S.numIslands(grid) == 1

    # Example 2
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert S.numIslands(grid) == 3

    print("All tests passed.")
