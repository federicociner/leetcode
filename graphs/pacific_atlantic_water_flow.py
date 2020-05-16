"""Given an m x n matrix of non-negative integers representing the height of
each unit cell in a continent, the "Pacific ocean" touches the left and top
edges of the matrix and the "Atlantic ocean" touches the right and bottom
edges.

Water can only flow in four directions (up, down, left, or right) from a cell
to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).

"""
from typing import List


class Solution:
    # Time complexity: O(M * N)
    # Space complexity: O(M * N)
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ans = []

        # Keep track of visited nodes
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        # Iterate through rows
        for row in range(m):
            self.dfs(matrix, p_visited, row, 0)
            self.dfs(matrix, a_visited, row, n - 1)

        # Iterate through columns
        for col in range(n):
            self.dfs(matrix, p_visited, 0, col)
            self.dfs(matrix, a_visited, m - 1, col)

        for row in range(m):
            for col in range(n):
                if p_visited[row][col] and a_visited[row][col]:
                    ans.append([row, col])

        return ans

    def dfs(
        self,
        matrix: List[List[int]],
        visited: List[List[bool]],
        row: int,
        col: int,
    ) -> None:
        m = len(matrix)
        n = len(matrix[0])
        visited[row][col] = True

        for direction in self.directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            # Skip if coordinates are out of bounds
            if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                continue

            # Skip if node has previously been visited or if new location has
            # a lower height than previous location
            if (
                visited[newRow][newCol]
                or matrix[newRow][newCol] < matrix[row][col]
            ):
                continue

            self.dfs(matrix, visited, newRow, newCol)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    matrix = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    assert S.pacificAtlantic(matrix) == expected

    print("All tests passed.")
