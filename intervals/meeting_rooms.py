"""Given an array of meeting time intervals consisting of start and end times [
[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

Example 1:

    Input: [[0,30],[5,10],[15,20]]
    Output: false

Example 2:

    Input: [[7,10],[2,4]]
    Output: true

"""
from typing import List


class Solution:
    # Time complexity: O(n * log(n))
    # Space complexity: O(n)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda i: i[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


if __name__ == "__main__":
    S = Solution()

    # Example 1
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert S.canAttendMeetings(intervals) is False

    # Example 2
    intervals = [[7, 10], [2, 4]]
    assert S.canAttendMeetings(intervals) is True

    print("All tests passed.")
