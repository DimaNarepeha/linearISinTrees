from TreeNode import Tree, TreeNode
from ThreeSets import stableSet



'''
     1
    2 5
   3 4 

'''
my_tree = Tree(1)  # Root node with data 1
my_tree.root.children.append(TreeNode(2))
my_tree.root.children.append(TreeNode(5))
node_two = my_tree.root.children[0]

node_two.children.append(TreeNode(3))
node_two.children.append(TreeNode(4))

print(my_tree)

print(stableSet(my_tree.root))


