from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_ = 0

        def dfs(node, path_sum):
            nonlocal sum_
            if node:
                new_path_sum = path_sum * 10 + node.val
                if node.left:
                    dfs(node.left, new_path_sum)
                if node.right:
                    dfs(node.right, new_path_sum)
                if not node.left and not node.right:
                    sum_ += new_path_sum

        dfs(root, 0)
        return sum_


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.sumNumbers(root))
    print(solution.sumNumbers(None))
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(solution.sumNumbers(root))
