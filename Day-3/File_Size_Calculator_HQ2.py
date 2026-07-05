# H2) File Size Calculator (Recursive Folder Size)
# Definition

# Recursion is a programming technique in which a function calls itself to solve a problem by breaking it into 
# smaller subproblems. It continues calling itself until it reaches a base case, where the recursion stops.

# In This Problem
# A folder can contain:

# Files
# Other folders (subfolders)

# To calculate the total size of a folder:

# If the item is a file, add its size.
# If the item is a folder, calculate its size recursively.
# Repeat until there are no more subfolders.

# This makes Recursion the best approach because a folder can contain folders inside folders.


def Calculate_Size(folder):

    total = 0

    for item in folder:

        if type(item) == int:
            total += item

        else:
            total += Calculate_Size(item)

    return total


# Folder Structure
folder = [100, 200, [50, [150]]]

#Dry Run
print("Total Folder Size:", Calculate_Size(folder), "MB")