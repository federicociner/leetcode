"""Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.

Example:

    Input:
    [
        1->4->5,
        1->3->4,
        2->6
    ]

    Output: 1->1->2->3->4->4->5->6

"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode(0)
        res = curr

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return res.next


if __name__ == "__main__":
    # Inputs
    l1 = ListNode(1)
    n1 = ListNode(4)
    n2 = ListNode(5)
    l1.next = n1
    n1.next = n2

    l2 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(4)
    l2.next = n1
    n1.next = n2

    l3 = ListNode(2)
    n1 = ListNode(6)
    l3.next = n1

    lists = [l1, l2, l3]

    # Output: 1->1->2->3->4->4->5->6
    expected = ListNode(1)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)
    expected.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    s = Solution()
    actual = s.mergeKLists(lists)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next
