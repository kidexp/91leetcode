from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        """
        recursive
        """
        result = []

        def dfs(root):
            if root is None:
                return
            result.append(root.val)
            if root.children:
                for child in root.children:
                    dfs(child)

        dfs(root)
        return result

    def preorder(self, root: "Node") -> List[int]:
        """
        iterative
        """
        result = []
        stack = []
        if root:
            stack.append(root)
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.children:
                    for child in node.children[::-1]:
                        stack.append(child)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(solution.preorder(root))
