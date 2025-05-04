from tree_node import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []

        return _inorder(self.root)

    def preorder(self):
        def _preorder(node):
            return [node.value] + _preorder(node.left) + _preorder(node.right) if node else []

        return _preorder(self.root)

    def postorder(self):
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.value] if node else []

        return _postorder(self.root)


# Example usage
bst = BST()
for val in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(val)

print("Inorder:  ", bst.inorder())  # [3, 5, 7, 10, 12, 15, 18]
print("Preorder: ", bst.preorder())  # [10, 5, 3, 7, 15, 12, 18]
print("Postorder:", bst.postorder())  # [3, 7, 5, 12, 18, 15, 10]
