"""String Obfuscation Module

Implements various string obfuscation techniques to hide payload intent:
- Random character insertion
- Character splitting and concatenation  
- Escape sequence obfuscation
- String reversal
"""

import random
import string
from typing import List, Tuple


class StringObfuscator:
    """Implements obfuscation techniques for strings."""
    
    def __init__(self, seed: int = None):
        """Initialize obfuscator with optional random seed.
        
        Args:
            seed: Random seed for reproducible obfuscation
        """
        if seed is not None:
            random.seed(seed)
    
    def random_char_insertion(self, payload: str, count: int = None) -> str:
        """Insert random characters into payload.
        
        Args:
            payload: Input string
            count: Number of random characters to insert (default: length/2)
            
        Returns:
            Obfuscated string with random characters
        """
        if count is None:
            count = max(1, len(payload) // 3)
        
        result = list(payload)
        for _ in range(count):
            pos = random.randint(0, len(result))
            char = random.choice(string.ascii_letters + string.digits)
            result.insert(pos, char)
        
        return ''.join(result)
    
    def char_splitting(self, payload: str, delimiter: str = '" "+"') -> str:
        """Split string and rejoin with delimiters.
        
        Args:
            payload: Input string
            delimiter: String to use for splitting
            
        Returns:
            Split and obfuscated string
        """
        return delimiter.join(payload)
    
    def string_reversal(self, payload: str) -> str:
        """Reverse the string.
        
        Args:
            payload: Input string
            
        Returns:
            Reversed string
        """
        return payload[::-1]
    
    def escape_sequence_obfuscation(self, payload: str) -> str:
        """Convert payload to escape sequences.
        
        Args:
            payload: Input string
            
        Returns:
            Obfuscated with escape sequences
        """
        result = []
        for char in payload:
            if char in ' \n\t\r':
                result.append(f'\\x{ord(char):02x}')
            else:
                result.append(char)
        return ''.join(result)
    
    def variable_concatenation(self, payload: str) -> Tuple[str, dict]:
        """Convert payload to variable concatenation.
        
        Args:
            payload: Input string
            
        Returns:
            Tuple of obfuscated code and variable mapping
        """
        variables = {}
        chunks = [payload[i:i+3] for i in range(0, len(payload), 3)]
        
        for i, chunk in enumerate(chunks):
            var_name = f'var_{i}'
            variables[var_name] = chunk
        
        obfuscated = ' + '.join([f'\'{v}\'' for v in variables.values()])
        return obfuscated, variables
    
    def unicode_obfuscation(self, payload: str) -> str:
        """Convert to unicode representation.
        
        Args:
            payload: Input string
            
        Returns:
            Unicode-obfuscated string
        """
        return ''.join(f'\\u{ord(char):04x}' for char in payload)
    
    def homograph_substitution(self, payload: str) -> str:
        """Replace similar-looking characters.
        
        Args:
            payload: Input string
            
        Returns:
            Homograph-substituted string
        """
        homographs = {
            '0': 'O',  # Zero to O
            '1': 'l',  # One to lowercase L
            '5': 'S',  # Five to S
            'O': '0',  # O to Zero
        }
        
        result = payload
        for old, new in homographs.items():
            result = result.replace(old, new)
        return result
    
    def case_variation(self, payload: str) -> str:
        """Apply random case variations.
        
        Args:
            payload: Input string
            
        Returns:
            Case-varied string
        """
        return ''.join(c.upper() if random.random() > 0.5 else c.lower() 
                      for c in payload)
    
    def comment_insertion(self, payload: str, language: str = 'python') -> str:
        """Insert comments between characters (for code).
        
        Args:
            payload: Input string
            language: Programming language ('python', 'bash', etc.)
            
        Returns:
            Code with inserted comments
        """
        if language == 'python':
            comment_sym = '#'
        elif language == 'bash':
            comment_sym = '#'
        else:
            comment_sym = '#'
        
        # For demonstration
        return f'{comment_sym} Obfuscated\n{payload}'
    
    def multi_layer_obfuscation(self, payload: str, methods: List[str]) -> str:
        """Apply multiple obfuscation methods sequentially.
        
        Args:
            payload: Input string
            methods: List of method names to apply
            
        Returns:
            Multi-layer obfuscated string
        """
        result = payload
        method_map = {
            'random_insert': self.random_char_insertion,
            'split': self.char_splitting,
            'reverse': self.string_reversal,
            'escape': self.escape_sequence_obfuscation,
            'unicode': self.unicode_obfuscation,
        }
        
        for method in methods:
            if method in method_map:
                result = method_map[method](result)
        
        return result


if __name__ == '__main__':
    obf = StringObfuscator()
    test = 'whoami'
    
    print(f"Original: {test}")
    print(f"Random Insert: {obf.random_char_insertion(test)}")
    print(f"Reversed: {obf.string_reversal(test)}")
    print(f"Unicode: {obf.unicode_obfuscation(test)}")
