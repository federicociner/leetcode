"""Remove all elements from a linked list of integers that have value val.

Example:

    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5

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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head

        prev = sentinel
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(6)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    actual = S.removeElements(n1, 6)

    expected = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    expected.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
