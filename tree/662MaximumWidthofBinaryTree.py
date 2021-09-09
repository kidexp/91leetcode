from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_gap = 0
        while queue:
            queue_size = len(queue)
            max_index = min_index = None
            for _ in range(queue_size):
                node, index = queue.pop()
                if max_index is None or index > max_index:
                    max_index = index
                if min_index is None or index < min_index:
                    min_index = index
                if node.left:
                    queue.appendleft((node.left, 2 * index))
                if node.right:
                    queue.appendleft((node.right, 2 * index + 1))
            max_gap = max(max_gap, max_index - min_index + 1)
        return max_gap


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(solution.widthOfBinaryTree(root))
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    print(solution.widthOfBinaryTree(root))
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    print(solution.widthOfBinaryTree(root))
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)
    print(solution.widthOfBinaryTree(root))
