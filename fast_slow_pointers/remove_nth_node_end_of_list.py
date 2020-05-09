"""Given a linked list, remove the n-th node from the end of list and return
its head.

Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes
    1->2->3->5.

Note:

    Given n will always be valid.

Follow up:

    Could you do this in one pass?

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        length = 0
        first = head

        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy

        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    actual = S.removeNthFromEnd(n1, 2)

    expected = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(5)
    expected.next = n2
    n2.next = n3
    n3.next = n4

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
