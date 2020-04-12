"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321
Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:

    Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
    of this problem, assume that your function returns 0 when the reversed
    integer overflows.

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        num = sign * int(str(abs(x))[::-1])

        int_min = -(2 ** 31)
        int_max = 2 ** 31 - 1

        return num if int_min < num < int_max else 0


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = 123
    assert s.reverse(x) == 321

    # Example 1
    x = -123
    assert s.reverse(x) == -321

    # Example 1
    x = 120
    assert s.reverse(x) == 21

    print("All tests passed.")
