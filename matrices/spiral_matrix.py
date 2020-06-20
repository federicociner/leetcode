"""Given a matrix of m x n elements (m rows, n columns), return all elements
of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        row_begin = 0
        row_end = len(matrix) - 1
        col_begin = 0
        col_end = len(matrix[0]) - 1

        while row_begin <= row_end and col_begin <= col_end:
            # Traverse right
            for i in range(col_begin, col_end + 1):
                ans.append(matrix[row_begin][i])

            row_begin += 1

            # Traverse down
            for i in range(row_begin, row_end + 1):
                ans.append(matrix[i][col_end])

            col_end -= 1

            # Traverse left
            if row_begin <= row_end:
                for i in reversed(range(col_begin, col_end + 1)):
                    ans.append(matrix[row_end][i])

            row_end -= 1

            # Traverse up
            if col_begin <= col_end:
                for i in reversed(range(row_begin, row_end + 1)):
                    ans.append(matrix[i][col_begin])

            col_begin += 1

        return ans


if __name__ == "__main__":
    S = Solution()

    # Example 1
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    actual = S.spiralOrder(matrix)

    assert actual == expected

    # Example 2
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    actual = S.spiralOrder(matrix)

    assert actual == expected

    print("All tests passed.")
