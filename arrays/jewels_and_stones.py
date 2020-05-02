"""You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of
stone you have.  You want to know how many of the stones you have are also
jewels.

The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".

Example 1:

    Input: J = "aA", S = "aAAbbbb"
    Output: 3

Example 2:

    Input: J = "z", S = "ZZ"
    Output: 0

Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

"""


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n)
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)

        return sum(s in jewels for s in S)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    J = "aA"
    S = "aAAbbbb"
    assert s.numJewelsInStones(J, S) == 3

    # Example 2
    J = "z"
    S = "ZZ"
    assert s.numJewelsInStones(J, S) == 0

    print("All tests passed.")
