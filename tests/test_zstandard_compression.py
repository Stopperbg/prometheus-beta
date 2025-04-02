import pytest
import zstandard as zstd
from src.zstandard_compression import compress_data, decompress_data


def test_basic_compression_and_decompression():
    """Test basic compression and decompression of a simple string."""
    original_data = "Hello, Zstandard compression!"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original_data


def test_binary_data_compression():
    """Test compression and decompression of binary data."""
    original_data = b'\x00\x01\x02\x03\xff\xfe\xfd'
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    
    decompressed = decompress_data(compressed)
    assert decompressed == original_data


def test_compression_levels():
    """Test different compression levels."""
    data = "Test compression levels" * 100
    
    for level in [1, 3, 5, 10, 22]:
        compressed = compress_data(data, compression_level=level)
        decompressed = decompress_data(compressed)
        assert decompressed.decode('utf-8') == data


def test_dictionary_compression():
    """Test compression and decompression with a dictionary."""
    dictionary = b"sample dictionary for compression"
    data = "Hello, compressed world!" * 10
    
    compressed = compress_data(data, dictionary=dictionary)
    decompressed = decompress_data(compressed, dictionary=dictionary)
    
    assert decompressed.decode('utf-8') == data


def test_invalid_compression_level():
    """Test handling of invalid compression levels."""
    with pytest.raises(ValueError, match="Compression level must be between 1 and 22"):
        compress_data("test", compression_level=0)
    
    with pytest.raises(ValueError, match="Compression level must be between 1 and 22"):
        compress_data("test", compression_level=23)


def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        compress_data(123)
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data("not bytes")


def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_str = ""
    empty_bytes = b""
    
    for data in [empty_str, empty_bytes]:
        compressed = compress_data(data)
        decompressed = decompress_data(compressed)
        assert decompressed == b""