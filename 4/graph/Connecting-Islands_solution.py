"""
:param: num_islands - number of islands
:param: bridge_config - bridge configuration as explained in the problem statement
return: cost (int) minimum cost of connecting all islands
TODO complete this method to returh minimum cost of connecting all islands
"""
# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    # A graph can be represented as a adjacency_list, which is a list of blank lists
    graph = [list() for _ in range(num_islands + 1)]
    
    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        
        # An entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))
           
    # Try this: print("graph = ",graph)
    return graph

def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """
    
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1
    
    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]
    
    # Heap is represented as a list of tuples 
    # A "node" in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)
        
        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)