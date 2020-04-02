"""Given a non-negative integer numRows, generate the first numRows of
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above
it.

Example:

    Input: 5
    Output:
    [
        [1],
       [1,1],
      [1,2,1],
     [1,3,3,1],
    [1,4,6,4,1]
    ]

"""
from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1 for _ in range(i + 1)] for i in range(numRows)]

        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        return pascal


if __name__ == "__main__":
    s = Solution()

    # Example 1
    numRows = 4
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert s.generate(numRows) == expected

    # Example 2
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert s.generate(numRows) == expected

    print("All tests passed.")
