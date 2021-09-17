from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mid_of_linked_list(head):
    if not head or not head.next:
        return head
    dummy_head = ListNode(0, head)
    slow = fast = dummy_head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mid


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        mid = find_mid_of_linked_list(head)
        if mid:
            root = TreeNode(mid.val)
            if head != mid:
                root.left = self.sortedListToBST(head)
            if mid.next:
                root.right = self.sortedListToBST(mid.next)
            return root
        else:
            return None


def iterate_tree(root):
    from collections import deque

    queue = deque([root])
    level = 0
    while queue:
        queue_size = len(queue)
        print(f"level {level}: ")
        for _ in range(queue_size):
            node = queue.pop()
            if node:
                print(node.val, end=" ")
                queue.appendleft(node.left)
                queue.appendleft(node.right)
        print()
        level += 1


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    iterate_tree(solution.sortedListToBST(head))
    iterate_tree(solution.sortedListToBST(None))
    ead = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(10)
    iterate_tree(solution.sortedListToBST(head))
