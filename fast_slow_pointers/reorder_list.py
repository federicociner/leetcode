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
    # Time complexity: O(n * log(n))
    # Space complexity: O(1)
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None

        # find middle of list
        middle = self.findMiddle(head)

        # reverse second half of list
        reverse = self.reverseList(middle)

        # merge two lists
        first = head
        second = reverse

        while second.next:
            dummy = first.next
            first.next = second
            first = dummy

            dummy = second.next
            second.next = first
            second = dummy

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def findMiddle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    S.reorderList(n1)
    actual = n1

    expected = ListNode(1)
    n2 = ListNode(6)
    n3 = ListNode(2)
    n4 = ListNode(5)
    n5 = ListNode(3)
    n6 = ListNode(4)
    expected.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    while expected:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next

    print("All tests passed.")
