# for the number of rows. Here is the sample program

"""
How tall is the tree: 5
    #
   ###
  #####
 #######
#########
    #
"""

"""
Patterns:
4 spaces : 1 hash
3 spaces : 3 hash
2 spaces : 5 hash
1 spaces : 7 hash
0 spaces : 9 hash
loop times = tree_height
spaces decrement by 1
hashes increment by 2
spaces before stump = 4
"""
# Get the number of rows for the tree
tree_height = input("How tall is the tree: ")
# Convert into an integer
tree_height = int(tree_height)
# initiate the spaces
spaces = tree_height - 1
# initiate the hashes
hashes = 1
# stump_spaces
stump_spaces = tree_height - 1
# while loop times equal to tree_height
while tree_height != 0:
    # print the spaces
    for i in range(spaces):
        print(' ', end='')
    # print the hashes
    for i in range(hashes):
        print('#', end='')
    # Newline after each row is printed
    print()
    # spaces decremented by 1(' ' -=1)
    spaces -= 1
    # hashes incremented by 2 (# +=2)
    hashes += 2
    # tree_height decremented by 1(-=1)
    tree_height -= 1
# print the spaces before the stump
for i in range(stump_spaces):
    print(' ', end='')
# then the hash
print('#')
