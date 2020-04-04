"""Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1,2,3]
    Output:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, len(nums), res)

        return res

    def backtrack(
        self, nums: List[int], first: int, n: int, res: List[List[int]],
    ):
        if first == n:
            res.append(nums[:])

        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(nums, first + 1, n, res)
            nums[first], nums[i] = nums[i], nums[first]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.permute([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
