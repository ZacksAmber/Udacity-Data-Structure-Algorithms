import math   # Need math.inf constant

def dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value 
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity 
    distance_dict = {node: math.inf for node in graph.nodes}
    
    
    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}

    distance_dict[start_node] = 0
    
    while distance_dict:
        
        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        
        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)

        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the alreday stored distance, update the distance_dict
        for edge in current_node.edges:
            if edge.node in distance_dict:
                
                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour
    
    return shortest_distance[end_node]