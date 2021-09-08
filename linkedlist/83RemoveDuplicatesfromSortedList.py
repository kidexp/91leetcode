from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        while cur:
            if cur.next is not None and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def iterate_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print("")
    print("===============")


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(4)
    iterate_linked_list(solution.deleteDuplicates(l1))
