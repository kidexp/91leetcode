from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        last_left_most_value = None
        queue = deque([root])
        while queue:
            queue_size = len(queue)
            last_left_most_value = queue[0].val
            for _ in range(queue_size):
                node = queue.pop()
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
        return last_left_most_value


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    print(solution.findBottomLeftValue(root))
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(solution.findBottomLeftValue(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(7)
    root.right.right = TreeNode(6)
    print(solution.findBottomLeftValue(root))
