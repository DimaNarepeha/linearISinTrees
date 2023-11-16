from TreeNode import Tree, TreeNode


def getArrayOfNodesFrom(node):
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


def verifyFileHasSpaceOrNewLineAtTheEnd(filepath):
    file = open(filepath, "r")

    lines = file.read()
    if lines[-1] != "\n" and lines[-1] != " ":
        raise Exception("File should end with newLine or space")
    file.close()


def getTreeFromFile(filepath):
    f = open(filepath, "r")
    verifyFileHasSpaceOrNewLineAtTheEnd(filepath)
    return parceTreeFromFile(f)


def parceTreeFromFile(f):
    tree_from_file = None

    # save all nodes in a list to search for ones that need to append childs
    all_nodes_list = {}
    for line in f:
        tree_from_file = parceLine(all_nodes_list, line, tree_from_file)
    return tree_from_file


def parceLine(all_nodes_list, line, tree_from_file):
    current_digit_str = ""

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
                # init child and append to parrent
                child = TreeNode(current_digit_str)
                parent.children.append(child)
                all_nodes_list[current_digit_str] = child
                current_digit_str = ""
                continue
            current_digit_str = ""
    return tree_from_file
