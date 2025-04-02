import zstandard as zstd
from typing import Union, Optional


def compress_data(data: Union[str, bytes], 
                  compression_level: int = 3, 
                  dictionary: Optional[bytes] = None) -> bytes:
    """
    Compress data using Zstandard compression algorithm.

    Args:
        data (Union[str, bytes]): The data to compress.
        compression_level (int, optional): Compression level (1-22). 
            Defaults to 3. Higher levels provide better compression 
            but take longer.
        dictionary (Optional[bytes], optional): Optional compression 
            dictionary to improve compression. Defaults to None.

    Returns:
        bytes: Compressed data

    Raises:
        ValueError: If compression level is out of valid range
        TypeError: If input data is not str or bytes
    """
    # Validate compression level
    if compression_level < 1 or compression_level > 22:
        raise ValueError("Compression level must be between 1 and 22")

    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Create Zstandard compressor
    if dictionary:
        cctx = zstd.ZstdCompressionContext()
        cctx.load_dictionary(dictionary)
        return cctx.compress(data, compression_level)
    else:
        return zstd.compress(data, compression_level)


def decompress_data(compressed_data: bytes, 
                    dictionary: Optional[bytes] = None) -> bytes:
    """
    Decompress Zstandard compressed data.

    Args:
        compressed_data (bytes): The data to decompress.
        dictionary (Optional[bytes], optional): Optional decompression 
            dictionary. Defaults to None.

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        zstd.ZstdError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Create Zstandard decompressor
    if dictionary:
        dctx = zstd.ZstdDecompressionContext()
        dctx.load_dictionary(dictionary)
        return dctx.decompress(compressed_data)
    else:
        return zstd.decompress(compressed_data)