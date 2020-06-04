"""We are given a list schedule of employees, which represents the working
time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are
in sorted order.

Return the list of finite intervals representing common, positive-length free
time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects
inside are Intervals, not lists or arrays. For example, schedule[0][0].start =
1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we
wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:

    Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    Output: [[3,4]]
    Explanation: There are a total of three employees, and all common free
    time intervals would be [-inf, 1], [3, 4], [10, inf]. We discard any
    intervals that contain inf as they aren't finite.

Example 2:

    Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    Output: [[5,6],[7,9]]

Constraints:

    1 <= schedule.length , schedule[i].length <= 50
    0 <= schedule[i].start < schedule[i].end <= 10^8

"""
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    # Time complexity: O(c * log(n))
    # Space complexity: O(n)
    def employeeFreeTime(
        self, schedule: List[List[Interval]]
    ) -> List[Interval]:
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        ans = []
        prev = ints[0]

        for curr in ints[1:]:
            if curr.start <= prev.end and curr.end > prev.end:
                prev.end = curr.end
            elif curr.start > prev.end:
                ans.append(Interval(prev.end, curr.start))
                prev = curr

        return ans


if __name__ == "__main__":
    S = Solution()

    # Example 1
    e1 = [Interval(1, 2), Interval(5, 6)]
    e2 = [Interval(1, 3)]
    e3 = [Interval(4, 10)]
    intervals = [e1, e2, e3]
    actual = S.employeeFreeTime(intervals)
    expected = [Interval(3, 4)]

    for i in range(len(expected)):

        assert actual[i].start == expected[i].start
        assert actual[i].end == expected[i].end

    # Example 2
    e1 = [Interval(1, 3), Interval(6, 7)]
    e2 = [Interval(2, 4)]
    e3 = [Interval(2, 5), Interval(9, 12)]
    intervals = [e1, e2, e3]
    actual = S.employeeFreeTime(intervals)
    expected = [Interval(5, 6), Interval(7, 9)]

    for i in range(len(expected)):
        assert actual[i].start == expected[i].start
        assert actual[i].end == expected[i].end

    print("All tests passed.")
