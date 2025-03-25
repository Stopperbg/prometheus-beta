import pytest
from src.linked_list_reversal import Node, reverse_linked_list

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to regular list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    head = Node(1)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [1]

def test_reverse_multiple_nodes():
    """Test reversing a list with multiple nodes."""
    # Create 1 -> 2 -> 3 -> 4 -> 5
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Check if the list is now 5 -> 4 -> 3 -> 2 -> 1
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_reverse_two_nodes():
    """Test reversing a list with two nodes."""
    head = create_linked_list([1, 2])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [2, 1]

def test_repeated_reversal():
    """Test that reversing twice returns the original list."""
    original_values = [1, 2, 3, 4, 5]
    head = create_linked_list(original_values)
    
    # Reverse once
    reversed_head = reverse_linked_list(head)
    
    # Reverse again
    double_reversed_head = reverse_linked_list(reversed_head)
    
    # Check if we get back the original list
    assert linked_list_to_list(double_reversed_head) == original_values