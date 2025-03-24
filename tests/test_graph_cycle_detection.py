import pytest
from src.graph_cycle_detection import detect_cycle_in_directed_graph

def test_cycle_detection_basic_cycle():
    """Test a simple graph with a cycle"""
    graph = {0: [1], 1: [2], 2: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_no_cycle():
    """Test a graph without a cycle"""
    graph = {0: [1], 1: [2], 2: [3]}
    assert detect_cycle_in_directed_graph(graph) == False

def test_cycle_detection_complex_cycle():
    """Test a more complex graph with a cycle"""
    graph = {0: [1], 1: [2], 2: [3], 3: [1]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_single_node_self_loop():
    """Test a single node with a self-loop"""
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_empty_graph():
    """Test an empty graph"""
    graph = {}
    assert detect_cycle_in_directed_graph(graph) == False

def test_cycle_detection_disconnected_graph():
    """Test a disconnected graph with a cycle"""
    graph = {0: [1], 1: [2], 2: [0], 3: [4], 4: [5]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_invalid_input_none():
    """Test handling of None input"""
    with pytest.raises(ValueError, match="Graph cannot be None"):
        detect_cycle_in_directed_graph(None)

def test_cycle_detection_invalid_input_not_dict():
    """Test handling of non-dictionary input"""
    with pytest.raises(ValueError, match="Graph must be a dictionary"):
        detect_cycle_in_directed_graph([1, 2, 3])