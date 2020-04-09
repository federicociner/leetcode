"""Reverse a singly linked list.

Example:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?

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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nextTmp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTmp

        return prev


if __name__ == "__main__":
    # Example
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # Output: 5->4->3->2->1->None
    expected = ListNode(5)
    n1 = ListNode(4)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(1)
    expected.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    actual = s.reverseList(head)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
