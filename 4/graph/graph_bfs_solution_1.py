# Solution
def bfs_search(root_node, search_value):
    visited = set()                           # Sets are faster while lookup. Lists are faster to iterate.
    queue = [root_node]
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:          # Lookup
                queue.append(child)
