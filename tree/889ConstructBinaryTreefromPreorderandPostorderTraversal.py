from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        left_root_val = preorder[1]
        left_root_index = postorder.index(left_root_val)
        root.left = self.constructFromPrePost(
            preorder[1 : 2 + left_root_index], postorder[:left_root_index]
        )
        root.right = self.constructFromPrePost(
            preorder[left_root_index + 2 :],
            postorder[left_root_index + 1 : len(postorder) - 1],
        )
        return root


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
        solution.constructFromPrePost(
            preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]
        )
    )
    level_traverse_tree(solution.constructFromPrePost(preorder=[1], postorder=[1]))
