"""Given a collection of intervals, find the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.

Example 1:

    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are
    non-overlapping.

Example 2:

    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals
    non-overlapping.

Example 3:

    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're
    already non-overlapping.

Note:

    You may assume the interval's end point is always bigger than its start
    point. Intervals like [1,2] and [2,3] have borders "touching" but they
    don't overlap each other.

"""
from typing import List


class Solution:
    # Time complexity: O(n * log(n))
    # Space complexity: O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1

        return len(intervals) - count


if __name__ == "__main__":
    S = Solution()

    # Example 1
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert S.eraseOverlapIntervals(intervals) == 1

    # Example 2
    intervals = [[1, 2], [1, 2], [1, 2]]
    assert S.eraseOverlapIntervals(intervals) == 2

    # Example 3
    intervals = [[1, 2], [2, 3]]
    assert S.eraseOverlapIntervals(intervals) == 0

    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    assert S.eraseOverlapIntervals(intervals) == 2

    print("All tests passed.")
