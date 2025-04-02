import pytest
from src.ford_fulkerson import ford_fulkerson

def test_simple_graph():
    """Test a simple graph with a known maximum flow."""
    graph = {
        'A': {'B': 10, 'C': 10},
        'B': {'D': 4, 'E': 8},
        'C': {'D': 12, 'E': 9},
        'D': {'F': 14},
        'E': {'F': 10},
        'F': {}
    }
    max_flow = ford_fulkerson(graph, 'A', 'F')
    assert max_flow == 19

def test_disconnected_graph():
    """Test a graph with no path from source to sink."""
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    max_flow = ford_fulkerson(graph, 'A', 'C')
    assert max_flow == 0

def test_single_path_graph():
    """Test a graph with a single path."""
    graph = {
        'A': {'B': 5},
        'B': {'C': 5},
        'C': {}
    }
    max_flow = ford_fulkerson(graph, 'A', 'C')
    assert max_flow == 5

def test_multiple_paths_graph():
    """Test a graph with multiple possible paths."""
    graph = {
        'A': {'B': 10, 'C': 10},
        'B': {'D': 4},
        'C': {'D': 8},
        'D': {'E': 15},
        'E': {}
    }
    max_flow = ford_fulkerson(graph, 'A', 'E')
    assert max_flow == 14

def test_invalid_source_node():
    """Test handling of invalid source node."""
    graph = {
        'A': {'B': 10},
        'B': {}
    }
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 'C', 'B')

def test_invalid_sink_node():
    """Test handling of invalid sink node."""
    graph = {
        'A': {'B': 10},
        'B': {}
    }
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 'A', 'C')

def test_zero_capacity_graph():
    """Test a graph with zero capacities."""
    graph = {
        'A': {'B': 0},
        'B': {}
    }
    max_flow = ford_fulkerson(graph, 'A', 'B')
    assert max_flow == 0