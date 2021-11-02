import sys

'''Find the shortest path from the source node to every other node in the given graph'''
def dijkstra(graph, source):
    
    result = {}
    result[source] = 0                 
    
    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize
            
    unvisited = set(graph.nodes)  
    
    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited: 
        min_node = None    
        
        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:
                
                if min_node is None:       
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break
            
        # known distance of min_node
        current_distance = result[min_node]
        
        # 2. For the current node, find all the unvisited neighbours. 
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]
            
                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node
        
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result