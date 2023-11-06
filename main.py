from TreeNode import Tree, TreeNode
from ThreeSets import stableSet



'''
     1
    2 5
   3 4 
   
   
1-5: 1,2,3,4,5
6: 2,5
7: 3,4
8: 3,5
9: 2,4
10: 1,3
11: 1,4
12: 1,3,4
13: 3,4,5
14: empty set
'''
my_tree = Tree(1)  # Root node with data 1
my_tree.root.children.append(TreeNode(2))
my_tree.root.children.append(TreeNode(5))
node_two = my_tree.root.children[0]

node_two.children.append(TreeNode(3))
node_two.children.append(TreeNode(4))

print(my_tree)

print(stableSet(my_tree.root))


