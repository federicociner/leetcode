"""Given a collection of intervals, merge all overlapping intervals.

Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,
    6].

Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        ans = []

        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans


if __name__ == "__main__":
    S = Solution()

    # Example 1
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert S.merge(intervals) == expected

    # Example 2
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    assert S.merge(intervals) == expected

    print("All tests passed.")
