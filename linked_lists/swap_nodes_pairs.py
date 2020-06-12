"""Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be
changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr = ListNode(-1)
        curr.next = head

        prev = curr

        while head and head.next:
            first = head
            second = head.next

            first.next = second.next
            second.next = first

            prev.next = second
            prev = first
            head = first.next

        return curr.next


if __name__ == "__main__":
    # Example
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    head.next = n1
    n1.next = n2
    n2.next = n3

    expected = ListNode(2)
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    expected.next = n1
    n1.next = n2
    n2.next = n3

    s = Solution()
    actual = s.swapPairs(head)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
