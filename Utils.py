from TreeNode import Tree, TreeNode


def setArrayOfNodesFrom(node):
    result_arr = []
    if not node:
        return result_arr

    queue = [node]

    while queue:
        current_level = []
        next_level = []

        for item in queue:
            current_level.append(item)
            for child in item.children:
                next_level.append(child)

        result_arr.extend(reversed(current_level))
        queue = next_level

    return result_arr


def getArrayOfNodesFrom(my_tree):
    pass


def getInputFromFile(filepath):
    tree_from_file = None
    # save all nodes in a list to search for ones that need to append childs
    all_nodes_list = {}
    f = open(filepath, "r")
    current_digit_str = ""
    for line in f:
        parent = None
        for char in line:
            # Check if the character is a digit and read it until space
            if char.isdigit():
                current_digit_str = current_digit_str + char
            else:
                # init root if not initialized yet
                if tree_from_file is None:
                    tree_from_file = Tree(current_digit_str)
                    all_nodes_list[current_digit_str] = tree_from_file.root
                    parent = tree_from_file.root
                    current_digit_str = ""
                    continue
                # try to get parent if it was created before
                # init parent if not initialized
                if parent is None:
                    parent = all_nodes_list.get(current_digit_str)

                if parent is None:
                    parent = TreeNode(current_digit_str)
                    all_nodes_list[current_digit_str] = parent
                    current_digit_str = ""
                    continue
                if parent.data != current_digit_str:
                    child = TreeNode(current_digit_str)
                    parent.children.append(child)
                    all_nodes_list[current_digit_str] = child
                    current_digit_str = ""
                    continue
                current_digit_str = ""
    return tree_from_file
# init child and append to parrent
