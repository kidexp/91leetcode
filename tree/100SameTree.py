from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                return (
                    root1.val == root2.val
                    and dfs(root1.left, root2.left)
                    and dfs(root1.right, root2.right)
                )
            return False

        return dfs(p, q)


if __name__ == "__main__":
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(solution.isSameTree(p, q))
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    print(solution.isSameTree(p, q))
    p = TreeNode(1)
    p.left = TreeNode(3)
    p.right = TreeNode(2)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(solution.isSameTree(p, q))