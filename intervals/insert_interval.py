"""Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,
    10].

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        output = []
        new_start, new_end = newInterval
        i = 0
        n = len(intervals)

        # add all intervals starting before newInterval
        while i < n and new_start > intervals[i][0]:
            output.append(intervals[i])
            i += 1

        # add newInterval, merge if necessary
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)

        while i < n:
            interval = intervals[i]
            start, end = interval
            i += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)

        return output


if __name__ == "__main__":
    S = Solution()

    # Example 1
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]
    assert S.insert(intervals, new_interval) == [[1, 2], [3, 10], [12, 16]]

    print("All tests passed.")
