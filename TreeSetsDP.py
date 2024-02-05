def combinationsWithoutCurrent(current):
    num = 1
    for child in current:
        num *= child.cachedWithoutValue + child.cachedWithValue
    return num


def combinationsWithCurrent(current):
    num = 1
    for child in current:
        num *= child.cachedWithoutValue
    return num


def getAllSetsCount(arrayOfNodes):
    for node in arrayOfNodes:
        with_current = combinationsWithCurrent(node)
        without_current = combinationsWithoutCurrent(node)
        node.cachedWithValue = with_current
        node.cachedWithoutValue = without_current
    # return root node calculated value [-1] is the last element which is root in this case
    return arrayOfNodes[-1].cachedWithValue + arrayOfNodes[-1].cachedWithoutValue
