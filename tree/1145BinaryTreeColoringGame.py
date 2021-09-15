from types import coroutine
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def find_node(root):
            if root is None:
                return None
            if root.val == x:
                return root
            left = find_node(root.left)
            right = find_node(root.right)
            return left or right

        def count_nodes(root):
            if not root:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)

        node = find_node(root)
        left_child_nodes = count_nodes(node.left)
        right_child_nodes = count_nodes(node.right)
        return (
            left_child_nodes > n / 2
            or right_child_nodes > n / 2
            or (n - left_child_nodes - right_child_nodes - 1) > n / 2
        )


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(solution.btreeGameWinningMove(root, n=11, x=3))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.btreeGameWinningMove(root=root, n=3, x=1))
