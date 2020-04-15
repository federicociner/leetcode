"""Given an array of integers that is already sorted in ascending order, find
two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may
    not use the same element twice.

Example:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            x = numbers[left] + numbers[right]

            if target == x:
                return [left + 1, right + 1]

            if x < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    numbers = [2, 7, 11, 15]
    target = 9
    assert s.twoSum(numbers, target) == [1, 2]

    # Example 2
    numbers = [3, 8, 9, 12, 15, 18]
    target = 26
    assert s.twoSum(numbers, target) == [2, 6]

    print("All tests passed.")