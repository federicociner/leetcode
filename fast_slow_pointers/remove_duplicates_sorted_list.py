"""Given a sorted linked list, delete all duplicates such that each element
appear only once.

Example 1:

    Input: 1->1->2
    Output: 1->2

Example 2:

    Input: 1->1->2->3->3
    Output: 1->2->3

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # print(head)
        return head


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3

    actual = S.deleteDuplicates(n1)

    expected = ListNode(1)
    n2 = ListNode(2)
    expected.next = n2

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    # Example 1
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    actual = S.deleteDuplicates(n1)

    expected = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    expected.next = n2
    n2.next = n3

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
