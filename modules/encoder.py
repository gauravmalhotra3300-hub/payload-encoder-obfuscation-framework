"""Payload Encoding Module

This module provides encoding and transformation techniques for payloads:
- Base64 encoding and decoding
- XOR encryption with custom keys
- ROT13 substitution cipher
- Multi-layer encoding chains
"""

import base64
import codecs
from typing import Union, List


class PayloadEncoder:
    """Handles payload encoding operations."""
    
    def __init__(self):
        """Initialize the encoder."""
        self.encoding_methods = {
            'base64': self.encode_base64,
            'xor': self.encode_xor,
            'rot13': self.encode_rot13
        }
    
    def encode_base64(self, payload: str, decode: bool = False) -> str:
        """Encode or decode payload using Base64.
        
        Args:
            payload: Input payload string
            decode: If True, decode; if False, encode
            
        Returns:
            Encoded or decoded payload string
        """
        try:
            if decode:
                return base64.b64decode(payload.encode()).decode()
            else:
                return base64.b64encode(payload.encode()).decode()
        except Exception as e:
            raise ValueError(f"Base64 encoding error: {str(e)}")
    
    def encode_xor(self, payload: str, key: str = 'secret', decode: bool = False) -> str:
        """Encode or decode payload using XOR encryption.
        
        Args:
            payload: Input payload string
            key: XOR key (string)
            decode: If True, decode; if False, encode
            
        Returns:
            Encoded or decoded payload string
        """
        if not key:
            raise ValueError("XOR key cannot be empty")
        
        result = []
        key_len = len(key)
        
        for i, char in enumerate(payload):
            key_char = key[i % key_len]
            xor_value = ord(char) ^ ord(key_char)
            if decode:
                result.append(chr(xor_value))
            else:
                result.append(f'{xor_value:02x}')
        
        return ''.join(result)
    
    def encode_rot13(self, payload: str) -> str:
        """Encode payload using ROT13 cipher.
        
        Args:
            payload: Input payload string
            
        Returns:
            ROT13 encoded payload
        """
        return codecs.encode(payload, 'rot_13')
    
    def decode_xor(self, payload: str, key: str = 'secret') -> str:
        """Decode XOR-encoded payload.
        
        Args:
            payload: Hex-encoded XOR payload
            key: XOR key (must match encoding key)
            
        Returns:
            Decoded payload string
        """
        result = []
        key_len = len(key)
        
        # Convert hex string back to bytes
        for i in range(0, len(payload), 2):
            hex_pair = payload[i:i+2]
            xor_value = int(hex_pair, 16)
            key_char = key[(i // 2) % key_len]
            decoded_char = chr(xor_value ^ ord(key_char))
            result.append(decoded_char)
        
        return ''.join(result)
    
    def encode_chain(self, payload: str, methods: List[tuple]) -> str:
        """Apply multiple encoding methods in sequence.
        
        Args:
            payload: Input payload
            methods: List of tuples (method_name, kwargs)
                     Example: [('base64', {}), ('xor', {'key': 'secret'})]
                     
        Returns:
            Multi-layer encoded payload
        """
        result = payload
        for method, kwargs in methods:
            if method not in self.encoding_methods:
                raise ValueError(f"Unknown encoding method: {method}")
            result = self.encoding_methods[method](result, **kwargs)
        return result
    
    def hex_encode(self, payload: str) -> str:
        """Encode payload to hex string.
        
        Args:
            payload: Input payload
            
        Returns:
            Hex-encoded payload
        """
        return payload.encode().hex()
    
    def hex_decode(self, payload: str) -> str:
        """Decode hex-encoded payload.
        
        Args:
            payload: Hex-encoded payload
            
        Returns:
            Decoded payload
        """
        return bytes.fromhex(payload).decode()
    
    def unicode_encode(self, payload: str) -> str:
        """Encode payload using unicode escapes.
        
        Args:
            payload: Input payload
            
        Returns:
            Unicode-encoded payload
        """
        return ''.join(f'\\u{ord(char):04x}' for char in payload)
    
    def get_encoding_info(self) -> dict:
        """Get information about available encoding methods.
        
        Returns:
            Dictionary with encoding method descriptions
        """
        return {
            'base64': 'Base64 encoding/decoding',
            'xor': 'XOR encryption with custom key',
            'rot13': 'ROT13 substitution cipher',
            'hex': 'Hexadecimal encoding',
            'unicode': 'Unicode escape encoding'
        }


if __name__ == '__main__':
    # Example usage
    encoder = PayloadEncoder()
    test_payload = 'whoami'
    
    print(f"Original: {test_payload}")
    print(f"Base64: {encoder.encode_base64(test_payload)}")
    print(f"ROT13: {encoder.encode_rot13(test_payload)}")
    print(f"XOR: {encoder.encode_xor(test_payload, key='secret')}")
    print(f"Hex: {encoder.hex_encode(test_payload)}")
