from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(
            inorder[root_index + 1 :], postorder[root_index : len(postorder) - 1]
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
        solution.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
    )
    level_traverse_tree(solution.buildTree(inorder=[-1], postorder=[-1]))
