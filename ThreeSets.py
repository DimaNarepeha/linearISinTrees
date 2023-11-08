def combinationsWithoutCurrent(current):
    if current.isCachedWithout:
        print("used cash for " + str(current.data))
        return current.cachedWithoutValue
    num = 1
    for child in current:
        num *= stableSet(child)
    current.cachedWithoutValue = num
    current.isCachedWithout = True
    print("calculated for " + str(current.data))
    return num


def combinationsWithCurrent(current):
    if current.isCachedWith:
        print("used cash for " + str(current.data))
        return current.cachedWithValue
    num = 1
    for child in current:
        num *= combinationsWithoutCurrent(child)
    current.cachedWithValue = num
    current.isCachedWith = True
    print("calculated for " + str(current.data))
    return num


def stableSet(current):
    return (combinationsWithCurrent(current) +
            combinationsWithoutCurrent(current))
