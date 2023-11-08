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


def getArrayOfNosdesFrom(my_tree):
    pass
