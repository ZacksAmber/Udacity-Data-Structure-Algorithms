# Solution
def dfs_recursion_start(start_node, search_value):
    visited = set()               # Set to keep track of visited nodes.
    return dfs_recursion(start_node, visited, search_value)

# Recursive function
def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        found = True              # Don't search in other branches, if found = True
        return node
    
    visited.add(node)
    found = False
    result = None

    # Conditional recurse on each neighbour
    for child in node.children:
        if (child not in visited):
                result = dfs_recursion(child, visited, search_value)
                
                # Once the match is found, no more recurse 
                if found:
                    break
    return result