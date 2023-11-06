class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __iter__(self):
        return iter(self.children)

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    
    def __str__(self):
        return self._str_helper(self.root)

    def _str_helper(self, node):
        result = str(node.data)
        if node.children:
            result += " ["
            result += ", ".join(self._str_helper(child) for child in node.children)
            result += "]"
        return result

# Create a tree with 5 nodes

if __name__ == "__main__":
# Adding child nodes
    my_tree = Tree(1)  # Root node with data 1
    my_tree.root.children.append(TreeNode(2))
    my_tree.root.children.append(TreeNode(3))
    my_tree.root.children.append(TreeNode(4))
    my_tree.root.children.append(TreeNode(5))

