"""Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.

Example:

    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

Note:

    - Only constant extra memory is allowed.
    - You may not alter the values in the list's nodes, only nodes itself may
    be changed.

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        k_tail = None
        new_head = None

        while curr:
            count = 0
            curr = head

            while count < k and curr:
                curr = curr.next
                count += 1

            if count == k:
                reversed_head = self.reverseList(head, k)

                if not new_head:
                    new_head = reversed_head

                if k_tail:
                    k_tail.next = reversed_head

                k_tail = head
                head = curr

        if k_tail:
            k_tail.next = head

        return new_head if new_head else head

    def reverseList(self, head: ListNode, k: int) -> ListNode:
        prev = None
        curr = head

        while k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1

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

    expected = ListNode(2)
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(5)
    expected.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    actual = s.reverseKGroup(head, 2)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
