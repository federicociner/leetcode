"""Given a singly linked list, determine if it is a palindrome.

Example 1:

    Input: 1->2
    Output: false

Example 2:

    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?

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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        # find first half and reverse second half
        first_half_end = self.findFirstHalfEnd(head)
        second_half_start = self.reverseList(first_half_end.next)

        # check whether there is a palindrome
        first = head
        second = second_half_start

        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

    def findFirstHalfEnd(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


if __name__ == "__main__":
    # Example 1
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(1)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    assert s.isPalindrome(head) is True

    # Example 2
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(1)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    assert s.isPalindrome(head) is False

    print("All tests passed.")
