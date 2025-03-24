from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph 
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the input graph is None or not a dictionary.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V) for tracking visited and recursion stack
    
    Example:
        >>> detect_cycle_in_directed_graph({0: [1], 1: [2], 2: [0]})
        True
        >>> detect_cycle_in_directed_graph({0: [1], 1: [2], 2: [3]})
        False
    """
    # Input validation
    if graph is None:
        raise ValueError("Graph cannot be None")
    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary")
    
    # If graph is empty, no cycle can exist
    if not graph:
        return False
    
    # Track visited nodes and nodes in current recursion stack
    visited = set()
    rec_stack = set()
    
    def dfs(node: int) -> bool:
        """
        Depth-first search to detect cycles
        
        Args:
            node (int): Current node to explore
        
        Returns:
            bool: True if cycle is found, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove node from recursion stack
        rec_stack.remove(node)
        return False
    
    # Check for cycles starting from each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False