# H3) Climbing the Staircase (Recursion)
# Definition

# Recursion is a programming technique in which a function calls itself to solve a problem by breaking it 
# into smaller subproblems. The recursive calls continue until a base case is reached.

# In This Problem

# A person wants to climb a staircase with N steps.

# Rules:

# You can climb 1 step at a time.
# Or 2 steps at a time.

# The task is to find the total number of different ways to reach the Nth step.

# Since the solution for the current step depends on the solutions of the previous two steps, Recursion is the most suitable approach.


def climb(n):

    if n==0 or n==1:
        return 1
    return climb(n-1)+climb(n-2)


n = int(input("Enter Number of Steps: "))

print("Total Ways =", climb(n))