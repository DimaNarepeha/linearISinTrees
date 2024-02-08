import timeit
from Utils import getArrayOfNodesFrom, getTreeFromFile
from TreeSetsDP import getAllSetsCount

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

#always add line at the end of your file



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

def write_to_file(data, filename="output.txt"):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Result written to {filename}")

def test_function():
    # Replace this with the actual test function logic
    import_setup = '''
from TreeSetsDP import getAllSetsCount
from Utils import getArrayOfNodesFrom, getTreeFromFile
tree_from_file = getTreeFromFile("input.txt")
arrayOfNodes = getArrayOfNodesFrom(tree_from_file.root)
    '''

    my_code = '''
allsetsCountDP = getAllSetsCount(arrayOfNodes[::-1])
    '''
    print(f"{timeit.timeit(setup=import_setup, stmt=my_code, number=1000) * 1000000000} nano seconds")

def real_function():
    # Replace this with the actual real function logic
    tree_from_file = getTreeFromFile("input.txt")
    arrayOfNodes = getArrayOfNodesFrom(tree_from_file.root)
    # reverse array. so that we start from the bottom of a tree
    allsetsCountDP = getAllSetsCount(arrayOfNodes[::-1])
    print(f"the IS count is {allsetsCountDP}")
    write_to_file(str(allsetsCountDP))

def main():
    # Asking user for the mode
    mode = input("Which mode do you want to run? (1 for Test Mode, 2 for Output Mode): ")

    if mode == "1":
        # Test Mode
        print("Test Mode Selected.")
        test_function()

    elif mode == "2":
        # Output Mode
        print("Output Mode Selected.")
        real_function()
    else:
        print("Invalid mode selected. Please choose 1 for Test Mode or 2 for Output Mode.")

if __name__ == "__main__":
    main()

