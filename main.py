#!/usr/bin/env python3
"""Main entry point for the framework."""

from modules.encoder import PayloadEncoder
from modules.obfuscator import StringObfuscator
from modules.evasion_tester import EvasionTester
from modules.reporter import ReportGenerator

def main():
    """Main demonstration."""
    print("\n=== Payload Encoder & Obfuscation Framework ===")
    
    payload = "whoami"
    encoder = PayloadEncoder()
    obfuscator = StringObfuscator()
    tester = EvasionTester()
    reporter = ReportGenerator()
    
    print(f"\nOriginal: {payload}")
    print(f"Base64: {encoder.encode_base64(payload)}")
    print(f"ROT13: {encoder.encode_rot13(payload)}")
    print(f"Detected: {tester.test_detection(payload)}")

if __name__ == '__main__':
    main()
