from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = None
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_index = i
        root.left = self.buildTree(preorder[1 : root_index + 1], inorder[:root_index])
        root.right = self.buildTree(
            preorder[root_index + 1 :], inorder[root_index + 1 :]
        )
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        simplify version
        """
        if not preorder:
            return None

        def build_tree(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])
            root = TreeNode(preorder[pre_start])
            root_index = None
            for i in range(in_start, in_end + 1):
                if inorder[i] == preorder[pre_start]:
                    root_index = i
            root.left = build_tree(
                pre_start + 1,
                pre_start + (root_index - in_start),
                in_start,
                root_index - 1,
            )
            root.right = build_tree(
                pre_start + (root_index - in_start) + 1,
                pre_end,
                root_index + 1,
                in_end,
            )
            return root

        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


def level_traverse_tree(root):
    from collections import deque, defaultdict

    if not root:
        print(None)
        return
    result = defaultdict(list)
    level = 0
    queue = deque([root])
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            node = queue.pop()
            result[level].append(node.val if node else None)
            if node:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
        print(level, result[level])
        level += 1


if __name__ == "__main__":
    solution = Solution()
    level_traverse_tree(
        solution.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    )
    level_traverse_tree(solution.buildTree(preorder=[-1], inorder=[-1]))
