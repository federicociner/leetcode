"""Given a set of distinct integers, nums, return all possible subsets (the
power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1,2,3]
    Output:
    [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        self.dfs(nums, 0, [], res)

        return res

    def dfs(
        self, nums: List[int], idx: int, p: List[int], res: List[List[int]]
    ):
        res.append(p)

        for i in range(idx, len(nums)):
            self.dfs(nums, i + 1, p + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
    actual = s.subsets([1, 2, 3])
    assert all(i in actual for i in expected)

    # Example 2
    expected = [[], [1], [1, 2], [2]]
    actual = s.subsets([1, 2])
    assert all(i in actual for i in expected)

    print("All tests passed.")
