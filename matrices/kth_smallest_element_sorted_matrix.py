"""Given a n x n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

"""
from typing import List, Tuple


class SolutionBinarySearch:
    # Time complexity: O(n * log(max - min))
    # Space complexity: O(1)
    def countLessEqual(
        self, matrix: List[List[int]], mid: int, smaller: int, larger: int
    ) -> Tuple[int, int, int]:
        count = 0
        n = len(matrix)
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(
                matrix, mid, smaller, larger
            )

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start


class SolutionSort:
    # Time complexity: O(n * log(n))
    # Space complexity: O(n)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0

        ans = []

        for row in matrix:
            ans += row

        return sorted(ans)[k - 1]


if __name__ == "__main__":
    S = SolutionBinarySearch()

    # Example 1
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    assert S.kthSmallest(matrix, k) == 13

    print("All tests passed.")
