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
    
    # Create a residual graph
    def create_residual_graph(graph):
        residual = {}
        for node in graph:
            residual[node] = {}
            for neighbor, capacity in graph[node].items():
                # Forward edge
                residual[node][neighbor] = capacity
                # Backward edge (if not exists)
                if neighbor not in residual:
                    residual[neighbor] = {}
                if node not in residual[neighbor]:
                    residual[neighbor][node] = 0
        return residual
    
    # Breadth-first search to find augmenting path
    def bfs(residual, source, sink):
        # Track visited nodes and parent nodes
        visited = {node: False for node in residual}
        parent = {node: None for node in residual}
        
        # Queue for BFS
        queue = deque([source])
        visited[source] = True
        
        while queue:
            current = queue.popleft()
            
            # Check neighbors
            for neighbor, capacity in residual[current].items():
                if not visited[neighbor] and capacity > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    
                    # Found path to sink
                    if neighbor == sink:
                        return parent
        
        # No path found
        return None
    
    # Initialize max flow
    max_flow = 0
    
    # Create residual graph
    residual = create_residual_graph(graph)
    
    # Find augmenting paths
    while True:
        # Find path using BFS
        parent = bfs(residual, source, sink)
        
        # No more augmenting paths
        if parent is None:
            break
        
        # Find minimum flow along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual[prev][current])
            current = prev
        
        # Update residual graph
        current = sink
        while current != source:
            prev = parent[current]
            residual[prev][current] -= path_flow
            residual[current][prev] += path_flow
            current = prev
        
        # Add to max flow
        max_flow += path_flow
    
    return max_flow