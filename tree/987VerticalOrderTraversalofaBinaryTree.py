from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_result = []
        queue = deque([(root, 0)])
        level = -1
        while queue:
            level += 1
            level_size = len(queue)
            for _ in range(level_size):
                node, v_level = queue.pop()
                level_result.append((v_level, level, node.val))
                if node.left:
                    queue.appendleft((node.left, v_level - 1))
                if node.right:
                    queue.appendleft((node.right, v_level + 1))
        level_result.sort()
        previous_v_level = None
        result = []
        for v_level, _, val in level_result:
            if v_level != previous_v_level:
                result.append([])
                previous_v_level = v_level
            if v_level == previous_v_level:
                result[-1].append(val)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.verticalTraversal(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(solution.verticalTraversal(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(solution.verticalTraversal(root))
