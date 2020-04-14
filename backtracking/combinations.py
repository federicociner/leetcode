"""Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

Example:

    Input: n = 4, k = 2
    Output:
    [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]

"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack([i for i in range(1, n + 1)], k, 0, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        k: int,
        index: int,
        sub: List[int],
        res: List[List[int]],
    ):
        if k == 0:
            res.append(sub)

        for i in range(index, len(nums)):
            self.backtrack(nums, k - 1, i + 1, sub + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.combine(4, 2)
    expected = [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
