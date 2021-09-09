from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0

        def dfs(root):
            nonlocal count
            if not root:
                return True, None
            if root.left is None and root.right is None:
                count += 1
                return True, root.val
            is_left_uni, left_val = dfs(root.left)
            is_right_uni, right_val = dfs(root.right)
            if is_left_uni and is_right_uni:
                if (
                    (left_val is None and root.val == right_val)
                    or (right_val is None and root.val == left_val)
                    or (left_val == right_val == root.val)
                ):
                    count += 1
                    return True, root.val
                return False, None
            else:
                return False, None

        dfs(root)
        return count


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print(solution.countUnivalSubtrees(root))
    print(solution.countUnivalSubtrees(None))
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print(solution.countUnivalSubtrees(root))
