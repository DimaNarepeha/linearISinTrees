class TreeNode:
    def __init__(self):
        self.child = []
        self.independent_sets = [0, 1]  # [0] = not included, [1] = included


def countIndependentSets(root):
    def dfs(node):
        for child in node.child:
            dfs(child)

        for i in range(2):  # 0 for not included, 1 for included
            total_sets = 1
            for child in node.child:
                if i == 0:
                    total_sets += (node.independent_sets[1] + child.independent_sets[0])
                else:
                    total_sets += (node.independent_sets[0] + child.independent_sets[0])
            node.independent_sets[i] = total_sets

    dfs(root)
    return root.independent_sets[0] + root.independent_sets[1]


# Example usage:
# Construct a tree and call the countIndependentSets function on the root node
root = TreeNode()
root.child = [TreeNode(), TreeNode(), TreeNode()]
# root.child[0].child = [TreeNode()]
# root.child[1].child = [TreeNode(), TreeNode()]
# root.child[1].child[1].child = [TreeNode()]

total_sets = countIndependentSets(root)
print("Total Independent Sets:", total_sets)