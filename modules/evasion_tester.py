modules/evasion_tester.py  """Evasion Testing Module

Simulates detection systems and tests payload evasion effectiveness.
"""

from typing import Dict, List, Tuple

class EvasionTester:
    """Tests payloads against simulated detection systems."""
    
    def __init__(self):
        self.signatures = [
            'whoami', 'tasklist', 'powershell', 'cmd.exe', 'nc.exe',
            'bash', 'sh', 'wget', 'curl', 'ncat'
        ]
        self.keywords = ['exec', 'system', 'subprocess', 'shell', 'eval']
    
    def test_detection(self, payload: str) -> bool:
        """Test if payload triggers detection.
        
        Args:
            payload: Payload string to test
            
        Returns:
            True if detected, False otherwise
        """
        payload_lower = payload.lower()
        
        # Check signatures
        for sig in self.signatures:
            if sig in payload_lower:
                return True
        
        # Check keywords
        for kw in self.keywords:
            if kw in payload_lower:
                return True
        
        return False
    
    def test_evasion_effectiveness(self, original: str, 
                                   obfuscated: str) -> Dict:
        """Compare evasion effectiveness.
        
        Args:
            original: Original payload
            obfuscated: Obfuscated payload
            
        Returns:
            Dictionary with detection results
        """
        original_detected = self.test_detection(original)
        obfuscated_detected = self.test_detection(obfuscated)
        
        return {
            'original_detected': original_detected,
            'obfuscated_detected': obfuscated_detected,
            'evasion_success': original_detected and not obfuscated_detected
        }

if __name__ == '__main__':
    tester = EvasionTester()
    print(tester.test_detection('whoami'))
    print(tester.test_detection('w0h0am0i'))
