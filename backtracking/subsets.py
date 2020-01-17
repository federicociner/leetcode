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

        # run DFS
        res = []
        self.dfs(nums, 0, [], res)

        return res

    def dfs(
        self, nums: List[int], index: int, p: List[int], res: List[List[int]]
    ):
        res.append(p)

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, p + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Examples
    res1 = s.subsets([1, 2, 3])

    assert all(
        i in res1
        for i in [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
    )
