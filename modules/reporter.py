"""Report Generation Module

Generates analysis reports for obfuscation and evasion testing results.
"""

import json
from datetime import datetime
from typing import Dict, List, Any

class ReportGenerator:
    """Generates reports from encoding and evasion testing results."""
    
    def __init__(self):
        self.report_data = {}
    
    def create_report(self, payload: str, encodings: Dict[str, str],
                      evasion_results: Dict[str, bool]) -> Dict[str, Any]:
        """Create a comprehensive report.
        
        Args:
            payload: Original payload
            encodings: Dictionary of encoding method results
            evasion_results: Evasion test results
            
        Returns:
            Report dictionary
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'original_payload': payload,
            'encoding_results': encodings,
            'evasion_results': evasion_results,
            'summary': {
                'total_encodings': len(encodings),
                'total_tests': len(evasion_results),
                'evasion_success_rate': self._calc_success_rate(evasion_results)
            }
        }
        return report
    
    def _calc_success_rate(self, results: Dict) -> float:
        if not results:
            return 0.0
        success_count = sum(1 for v in results.values() if v)
        return (success_count / len(results)) * 100
    
    def save_report(self, report: Dict, filename: str) -> str:
        """Save report to JSON file."""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        return filename
