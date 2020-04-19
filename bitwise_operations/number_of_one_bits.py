"""Write a function that takes an unsigned integer and return the number of
'1' bits it has (also known as the Hamming weight).



Example 1:

    Input: 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has
    a total of three '1' bits.

Example 2:

    Input: 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has
    a total of one '1' bit.

Example 3:

    Input: 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has
    a total of thirty one '1' bits.

Follow up:

    If this function is called many times, how would you optimize it?

"""


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count


if __name__ == "__main__":
    s = Solution()

    # Example 1
    n = int("00000000000000000000000000001011", 2)
    assert s.hammingWeight(n) == 3

    # Example 2
    n = int("11111111111111111111111111111101", 2)
    assert s.hammingWeight(n) == 31

    print("All tests passed.")
