import os
from random import randint

from TreeNode import Tree, TreeNode


def generateTree(output_file, max_number):
    # Generate a random tree structure
    tree = generateRandomTreeBoundNumber(max_number)
    # Write the tree to the output file
    writeTreeToFile(tree, output_file)

def generateRandomTree(levels, maxChildsPerNode):
    node_count = 0
    root_data = str(0)
    tree = Tree(root_data)
    node_count += 1
    nodes_at_level = []
    nodes_at_next_level = []
    # Generate nodes and edges randomly
    for level in range(1, levels):
        if level == 1:
            nodes_at_level = [tree.root]

        if len(nodes_at_next_level) == 0:
            for node in nodes_at_level:
                for num_of_childs in range( maxChildsPerNode):
                    child_data = str(node_count)
                    node_count += 1
                    child = TreeNode(child_data)
                    node.children.append(child)
                    nodes_at_next_level.append(child)
            nodes_at_level = []
        else:
            for node in nodes_at_next_level:
                for num_of_childs in range(maxChildsPerNode):
                    child_data = str(node_count)
                    node_count += 1
                    child = TreeNode(child_data)
                    node.children.append(child)
                    nodes_at_level.append(child)
            nodes_at_next_level = []

    return tree, node_count

def generateRandomTreeBoundNumber(maxNodeCount):
    node_count = 0
    node_count += 1
    root_data = str(node_count)
    tree = Tree(root_data)
        
    level = [tree.root]

    while node_count < maxNodeCount:
        next_level = []
        for node in level:
            for _ in range(randint(1, 3)):
                node_count += 1
                if node_count > maxNodeCount:
                    return tree
                child = TreeNode(node_count)
                node.children.append(child)
                next_level.append(child)
        level = next_level


def getNodesAtLevel(root, level):
    if level == 1:
        return [root]
    nodes = []
    for child in root.children:
        nodes.extend(getNodesAtLevel(child, level - 1))
    return nodes


def writeTreeToFile(tree, output_file):
    with open(output_file, 'w') as file:
        writeTreeToFileRecursive(tree.root, file)


def writeTreeToFileRecursive(node, file):
    file.write(str(node.data))

    for child in node.children:
        # writeTreeToFileRecursive(child, file, indent + 1)
        file.write(' ' + str(child.data))
    file.write('\n')
    for child in node.children:
        writeTreeToFileRecursive(child, file)


#numberOfLevels = int(input("Please enter number of levels and press enter:\n"))
#axChildsPerNode = int(input("Please enter max childs per node and press enter:\n"))
# Example usage:
numberOfNodes = int(input("Please enter number of the nodes:\n"))
generateTree("input.txt", numberOfNodes)
