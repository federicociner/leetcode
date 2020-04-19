"""Reverse bits of a given 32 bits unsigned integer.

Example 1:

    Input: 00000010100101000001111010011100
    Output: 00111001011110000010100101000000
    Explanation: The input binary string 00000010100101000001111010011100
    represents the unsigned integer 43261596, so return 964176192 which its
    binary representation is 00111001011110000010100101000000.

Example 2:

    Input: 11111111111111111111111111111101
    Output: 10111111111111111111111111111111
    Explanation: The input binary string 11111111111111111111111111111101
    represents the unsigned integer 4294967293, so return 3221225471 which its
    binary representation is 10111111111111111111111111111111.

"""


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31

        while n:
            ans += (n & 1) << power
            n >>= 1
            power -= 1

        return ans


if __name__ == "__main__":
    s = Solution()

    # Example 1
    n = int("00000010100101000001111010011100", 2)
    assert s.reverseBits(n) == 964176192

    # Example 2
    n = int("11111111111111111111111111111101", 2)
    assert s.reverseBits(n) == 3221225471

    print("All tests passed.")
