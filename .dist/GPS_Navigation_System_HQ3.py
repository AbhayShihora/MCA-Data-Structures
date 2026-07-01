# Definition

# Backtracking is a problem-solving technique in which we return to a previous state when needed. 
# It is commonly implemented using a Stack, which follows the LIFO (Last In, First Out) principle.

# In this Problem

# The GPS stores the places visited by the user.

# visit(place) → Move to a new place.
# back() → Return to the previously visited place.
# forward() → Move forward again if available.

# This works like the Back and Forward buttons of a web browser. Therefore, two stacks are used:

# Back Stack → Stores previously visited places.
# Forward Stack → Stores places that can be revisited.

backword=[]
forword=[]
current=None

