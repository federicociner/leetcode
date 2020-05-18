"""Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

Example 2:

    Input: [[7,10],[2,4]]
    Output: 1

"""
import heapq
from typing import List


class Solution:
    # Time complexity: O(n * log(n))
    # Space complexity: O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda i: i[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, intervals[i][1])

        return len(free_rooms)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert S.minMeetingRooms(intervals) == 2

    # Example 2
    intervals = [[7, 10], [2, 4]]
    assert S.minMeetingRooms(intervals) == 1

    print("All tests passed.")
