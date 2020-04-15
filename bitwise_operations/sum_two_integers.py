"""Calculate the sum of two integers a and b, but you are not allowed to use
the operator + and -.

Example 1:

    Input: a = 1, b = 2
    Output: 3

Example 2:

    Input: a = -2, b = 3
    Output: 1

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b

        if b == 0:
            return a

        mask = (2 ** 32) - 1

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & mask) if b > 0 else a


if __name__ == "__main__":
    s = Solution()

    # Example 1
    a = 1
    b = 2

    assert s.getSum(a, b) == 3

    # Example 2
    a = 2
    b = 3

    assert s.getSum(a, b) == 5

    # Example 3
    a = -1
    b = 1

    assert s.getSum(a, b) == 0

    print("All tests passed.")
