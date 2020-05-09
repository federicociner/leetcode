"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        curr = ListNode(0)
        ans = curr

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return ans.next


if __name__ == "__main__":
    S = Solution()

    # Example 1
    l1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    l1.next = n2
    n2.next = n3

    l2 = ListNode(5)
    n2 = ListNode(6)
    n3 = ListNode(4)
    l2.next = n2
    n2.next = n3

    actual = S.addTwoNumbers(l1, l2)

    expected = ListNode(7)
    n2 = ListNode(0)
    n3 = ListNode(8)
    expected.next = n2
    n2.next = n3

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
