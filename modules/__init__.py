"""Payload Encoder & Obfuscation Framework Modules

This package contains the core modules for payload encoding, obfuscation,
evasion testing, and reporting functionality.
"""

from .encoder import PayloadEncoder
from .obfuscator import StringObfuscator
from .evasion_tester import EvasionTester
from .reporter import ReportGenerator

__version__ = '1.0.0'
__author__ = 'Cybersecurity Research Team'
__all__ = ['PayloadEncoder', 'StringObfuscator', 'EvasionTester', 'ReportGenerator']
