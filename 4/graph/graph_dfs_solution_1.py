# Solution                
def dfs_search(root_node, search_value):
    visited = set()                         # Sets are faster for lookups
    stack = [root_node]                     # Start with a given root node
    
    while len(stack) > 0:                   # Repeat until the stack is empty
            
        current_node = stack.pop()          # Pop out a node added recently 
        visited.add(current_node)           # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before, and not available in the stack already.
            if (child not in visited) and (child not in stack):         
                stack.append(child)
                