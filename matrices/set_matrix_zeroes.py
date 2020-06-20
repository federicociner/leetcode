"""Given a m x n matrix, if an element is 0, set its entire row and column to
0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

    - A straight forward solution using O(mn) space is probably a bad idea.
    - A simple improvement uses O(m + n) space, but still not the best
    solution.
    - Could you devise a constant space solution?

"""
from typing import List


class Solution:
    # Time complexity: O(m x n)
    # Space complexity: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        is_col = False

        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if is_col:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    S = Solution()

    # Example 1
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    S.setZeroes(matrix)

    assert matrix == expected

    # Example 2
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    S.setZeroes(matrix)

    assert matrix == expected

    print("All tests passed.")
