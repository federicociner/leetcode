"""Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # numbers are in descending order, return reversed list
        if i == 0:
            nums.reverse()

            return

        k = i - 1  # last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1

        # swap numbers
        nums[k], nums[j] = nums[j], nums[k]

        # reverse the second part
        left = k + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [1, 2, 3]
    S.nextPermutation(nums)
    assert nums == [1, 3, 2]

    # Example 2
    nums = [3, 2, 1]
    S.nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    S.nextPermutation(nums)
    assert nums == [1, 5, 1]

    print("All tests passed.")
