# Definition for singly-linked list.
from typing import List


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = fast = dummy_head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    print(solution.middleNode(head).val)
    head.next = ListNode(2)
    print(solution.middleNode(head).val)
    head.next.next = ListNode(3)
    print(solution.middleNode(head).val)
    head.next.next.next = ListNode(4)
    print(solution.middleNode(head).val)
