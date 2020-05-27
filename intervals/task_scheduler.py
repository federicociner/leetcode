"""Given a char array representing tasks CPU need to do. It contains capital
letters A to Z where different letters represent different tasks. Tasks could
be done without original order. Each task could be done in one interval. For
each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two
same tasks, there must be at least n intervals that CPU are doing different
tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish
all the given tasks.

Example:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

"""
from heapq import heappush, heappop
from collections import Counter
from typing import List


class Solution:
    # Time complexity: O(n * log(n))
    # Space complexity: O(n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        curr_time = 0
        curr_heap = []

        for k, v in Counter(tasks).items():
            heappush(curr_heap, (-1 * v, k))

        while curr_heap:
            index = 0
            tmp = []

            while index <= n:
                curr_time += 1

                if curr_heap:
                    timing, task_id = heappop(curr_heap)

                    if timing != -1:
                        tmp.append((timing + 1, task_id))

                if not curr_heap and not tmp:
                    break
                else:
                    index += 1

            for item in tmp:
                heappush(curr_heap, item)

        return curr_time

    def leastIntervalSecond(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        most_frequent_task = max(task_counts)
        most_frequent_count = task_counts.count(most_frequent_task)

        return max(
            len(tasks),
            (most_frequent_task - 1) * (n + 1) + most_frequent_count,
        )


if __name__ == "__main__":
    S = Solution()

    # Example 1
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    assert S.leastIntervalSecond(tasks, n) == 8

    print("All tests passed.")
