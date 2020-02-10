"""Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be
a unique set of numbers.

Note:
    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

    Input: k = 3, n = 7
    Output: [[1,2,4]]

Example 2:

    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]

"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtrack([i for i in range(1, 10)], k, n, 0, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        k: int,
        n: int,
        index: int,
        sub: List[int],
        res: List[List[int]],
    ):
        if k < 0 or n < 0:
            return

        if k == 0 and n == 0:
            res.append(sub)

        for i in range(index, len(nums)):
            self.backtrack(
                nums, k - 1, n - nums[i], i + 1, sub + [nums[i]], res
            )


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.combinationSum3(3, 7)
    expected = [[1, 2, 4]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    actual = s.combinationSum3(3, 9)
    expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)
