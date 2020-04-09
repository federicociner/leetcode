"""Given a non-empty array of digits representing a non-negative integer, plus
one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.

Example 1:

    Input: [1,2,3]
    Output: [1,2,4]

    Explanation: The array represents the integer 123.

Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            index = n - i - 1

            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1

                return digits

        return [1] + digits


if __name__ == "__main__":
    s = Solution()

    # Example 1
    digits = [1, 2, 3]
    assert s.plusOne(digits) == [1, 2, 4]

    # Example 2
    digits = [4, 3, 2, 1]
    assert s.plusOne(digits) == [4, 3, 2, 2]

    # Example 3
    digits = [2, 1, 9]
    assert s.plusOne(digits) == [2, 2, 0]

    # Example 3
    digits = [9, 9, 9, 9, 9]
    assert s.plusOne(digits) == [1, 0, 0, 0, 0, 0]

    print("All tests passed.")
