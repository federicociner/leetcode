"""Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        curr = head
        prev = None

        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1
            n -= 1

        tail = curr
        con = prev

        while n:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr

        return head


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
    expected = ListNode(1)
    n1 = ListNode(4)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(5)
    expected.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    actual = s.reverseBetween(head, 2, 4)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
