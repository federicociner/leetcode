"""Write a function that reverses a string. The input string is given as an
array of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ASCII characters.

Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    A = ["h", "e", "l", "l", "o"]
    expected = ["o", "l", "l", "e", "h"]
    s.reverseString(A)

    assert A == expected

    # Example 2
    B = ["H", "a", "n", "n", "a", "h"]
    expected = ["h", "a", "n", "n", "a", "H"]
    s.reverseString(B)

    assert B == expected

    print("All tests passed.")
