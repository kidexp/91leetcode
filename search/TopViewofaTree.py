from collections import deque


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        if not root:
            return []
        top_view_dict = {}
        queue = deque([(root, 0)])
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                node, vertical_level = queue.pop()
                if vertical_level not in top_view_dict:
                    top_view_dict[vertical_level] = node.val
                if node.left:
                    queue.appendleft((node.left, vertical_level - 1))
                if node.right:
                    queue.appendleft((node.right, vertical_level + 1))
        result = []
        for i in range(min(top_view_dict), max(top_view_dict) + 1):
            result.append(top_view_dict[i])
        return result


if __name__ == "__main__":
    solution = Solution()
    root = None
    print(solution.solve(root))
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.right = Tree(4)
    root.left.right.right = Tree(5)
    root.left.right.right.right = Tree(6)
    root.left.right.right.right.right = Tree(7)
    print(solution.solve(root))
    root = Tree(3)
    root.left = Tree(1)
    root.right = Tree(4)
    root.left.left = Tree(0)
    root.left.right = Tree(2)
    print(solution.solve(root))
