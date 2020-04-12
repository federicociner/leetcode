"""Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:

    Input: "race a car"
    Output: false

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            elif not s[left].isalnum():
                left += 1
            else:
                right -= 1

        return True


if __name__ == "__main__":
    s = Solution()

    # Example 1
    S = "A man, a plan, a canal: Panama"
    assert s.isPalindrome(S) is True

    # Example 2
    S = "race a car"
    assert s.isPalindrome(S) is False

    print("All tests passed.")
