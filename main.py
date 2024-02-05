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

# reverse array. so that we start from the bottom of a tree
import_setup = '''
from TreeSetsDP import getAllSetsCount
from Utils import getArrayOfNodesFrom, getTreeFromFile
tree_from_file = getTreeFromFile("input.txt")
arrayOfNodes = getArrayOfNodesFrom(tree_from_file.root)
'''

my_code = '''
allsetsCountDP = getAllSetsCount(arrayOfNodes[::-1])
'''
print(timeit.timeit(setup=import_setup, stmt=my_code, number=1000) * 1000000000)
# Specify the file path
file_path = 'output.txt'

# Open the file in write mode
#with open(file_path, 'w') as file:
#    # Write the number to the file
#    file.write(str(allsetsCountDP))
