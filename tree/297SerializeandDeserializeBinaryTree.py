# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import json


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        encode_list = []
        level_list = [root]
        while level_list:
            level_size = len(level_list)
            next_level = []
            for i in range(level_size):
                if level_list[i]:
                    encode_list.append(level_list[i].val)
                    next_level.append(level_list[i].left)
                    next_level.append(level_list[i].right)
                else:
                    encode_list.append(None)
            level_list = next_level
        return json.dumps(encode_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        encode_list = json.loads(data)
        if encode_list[0] is None:
            return None
        root = TreeNode(encode_list[0])
        current_level_node_list = [root]
        index = 1
        while index < len(encode_list):
            next_level_node_list = []
            for node in current_level_node_list:
                node.left = (
                    TreeNode(encode_list[index])
                    if encode_list[index] is not None
                    else None
                )
                node.right = (
                    TreeNode(encode_list[index + 1])
                    if encode_list[index + 1] is not None
                    else None
                )
                if node.left:
                    next_level_node_list.append(node.left)
                if node.right:
                    next_level_node_list.append(node.right)
                index += 2
            current_level_node_list = next_level_node_list
        return root


def bfs(root):
    if not root:
        return None
    result = []
    level_list = [root]
    while level_list:
        level_size = len(level_list)
        next_level = []
        for i in range(level_size):
            if level_list[i]:
                result.append(level_list[i].val)
                next_level.append(level_list[i].left)
                next_level.append(level_list[i].right)
            else:
                result.append(None)
        level_list = next_level
    return result


if __name__ == "__main__":
    solution = Codec()
    root = None
    serialized_string = solution.serialize(root)
    print(f"after serialize: {serialized_string}")
    data = bfs(solution.deserialize(serialized_string))
    print(f"after desexualization: {data}")
    root = TreeNode(1)
    serialized_string = solution.serialize(root)
    print(f"after serialize: {serialized_string}")
    data = bfs(solution.deserialize(serialized_string))
    print(f"after desexualization: {data}")
    root = TreeNode(1)
    root.left = TreeNode(2)
    serialized_string = solution.serialize(root)
    print(f"after serialize: {serialized_string}")
    data = bfs(solution.deserialize(serialized_string))
    print(f"after desexualization: {data}")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    serialized_string = solution.serialize(root)
    print(f"after serialize: {serialized_string}")
    data = bfs(solution.deserialize(serialized_string))
    print(f"after desexualization: {data}")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    serialized_string = solution.serialize(root)
    print(f"after serialize: {serialized_string}")
    data = bfs(solution.deserialize(serialized_string))
    print(f"after desexualization: {data}")
