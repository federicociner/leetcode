"""Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4

Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # split list in half
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reduce size of second half
        second = slow.next
        slow.next = None

        # recursive calls to merge
        left = self.sortList(head)
        right = self.sortList(second)

        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if not left or not right:
            return left or right

        if left.val > right.val:
            left, right = right, left

        head = left
        curr = left
        left = left.next

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left or right

        return head


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    actual = S.sortList(n1)

    expected = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    expected.next = n2
    n2.next = n3
    n3.next = n4

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
