from TreeNode import Tree, TreeNode
from TreeSetsDP import getAllSetsCount
from TreeSetsWithCache import stableSet
from Utils import setArrayOfNodesFrom

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

#
#     1
#  2     3
# 4 5   6 7

my_tree = Tree(1)  # Root node with data 1
my_tree.root.children.append(TreeNode(2))
my_tree.root.children.append(TreeNode(3))

child2 = my_tree.root.children[0]
child3 = my_tree.root.children[1]

child2.children.append(TreeNode(4))
child2.children.append(TreeNode(5))

child3.children.append(TreeNode(6))
child3.children.append(TreeNode(7))

# my_tree = Tree(1)  # Root node with data 1
# my_tree.root.children.append(TreeNode(2))
# my_tree.root.children.append(TreeNode(5))
# node_two = my_tree.root.children[0]
#
# node_two.children.append(TreeNode(3))
# node_two.children.append(TreeNode(4))

print(my_tree)

print(stableSet(my_tree.root))

# DP Algorithm:
# the function should reseive an array of nodes that goes from bottom to the top level by level
# it is very important for the algorithm to work
# Example:
#     1
#  2     3
# 4 5   6 7
# For this tree our array will look like this:
# 7,6,3,4,5,2,1
# It could look also like this:
# 7,6,5,4,3,2,1
# the only important property is that child should always be earlier to the parent


#     1
#  2     3
# 4 5   6 7

my_tree = Tree(1)  # Root node with data 1
my_tree.root.children.append(TreeNode(2))
my_tree.root.children.append(TreeNode(3))

child2 = my_tree.root.children[0]
child3 = my_tree.root.children[1]

child2.children.append(TreeNode(4))
child2.children.append(TreeNode(5))

child3.children.append(TreeNode(6))
child3.children.append(TreeNode(7))

arrayOfNodes = setArrayOfNodesFrom(my_tree.root)
print(arrayOfNodes)
# reverse array. so that we start from the bottom of a tree
allsetsCountDP = getAllSetsCount(arrayOfNodes[::-1])
print(allsetsCountDP)