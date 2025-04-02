from typing import List, Dict
from collections import deque

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dicts of neighbors 
                                           with their edge capacities.
        source (str): The source node.
        sink (str): The sink node.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a deep copy of the graph to create a residual graph
    def create_residual_graph(graph):
        residual = {}
        # Ensure all nodes are in the residual graph
        all_nodes = set(graph.keys()).union(
            set(node for subdict in graph.values() for node in subdict)
        )
        
        # Initialize residual graph with all nodes
        for node in all_nodes:
            residual[node] = {}
        
        # Add forward and backward edges
        for node in graph:
            for neighbor, capacity in graph[node].items():
                # Forward edge
                residual[node][neighbor] = capacity
                # Ensure backward edge exists
                if node not in residual[neighbor]:
                    residual[neighbor][node] = 0
        
        return residual
    
    # Depth-first search to find augmenting path
    def dfs(residual, source, sink, path, visited):
        # Mark source as visited
        visited.add(source)
        
        # If we've reached the sink, return the path
        if source == sink:
            return path
        
        # Explore all neighboring nodes
        for neighbor, capacity in residual[source].items():
            if neighbor not in visited and capacity > 0:
                # Try to extend the path
                new_path = dfs(residual, neighbor, sink, path + [(source, neighbor)], visited)
                
                # If a path is found, return it
                if new_path:
                    return new_path
        
        # No path found
        return None
    
    # Initialize max flow
    max_flow = 0
    
    # Create residual graph
    residual = create_residual_graph(graph)
    
    # Find augmenting paths
    while True:
        # Find path using DFS
        visited = set()
        path = dfs(residual, source, sink, [], visited)
        
        # No more augmenting paths
        if not path:
            break
        
        # Find minimum flow along the path
        path_flow = min(residual[u][v] for u, v in path)
        
        # Update residual graph
        for u, v in path:
            # Reduce forward edge capacity
            residual[u][v] -= path_flow
            
            # Ensure backward edge exists
            if v not in residual[u]:
                residual[u][v] = 0
            
            # Increase backward edge capacity
            residual[v][u] += path_flow
        
        # Add to max flow
        max_flow += path_flow
    
    return max_flow