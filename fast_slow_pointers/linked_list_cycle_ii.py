"""Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to
    the second node.


Example 2:

    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to
    the first node.


Example 3:

    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Follow-up:

    Can you solve it without using extra space?

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
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        intersection = self.get_intersection(head)

        if not intersection:
            return None

        p1 = head
        p2 = intersection

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

    def get_intersection(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return slow

        return None


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    assert S.detectCycle(n1) == n2

    print("All tests passed.")
