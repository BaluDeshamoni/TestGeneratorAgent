import xml.etree.ElementTree as ET
from pathlib import Path

def analyze_results(test_output, coverage_report):
    """Parse test failures and coverage gaps."""
    issues = []
    
    # Parse test failures
    if "FAILURES" in test_output["stderr"] or "ERRORS" in test_output["stderr"]:
        failures = [line for line in test_output["stderr"].splitlines() if "FAILED" in line or "ERROR" in line]
        issues.append({"type": "failure", "details": failures})
    
    # Parse coverage
    coverage_percentage = 0
    uncovered_lines = []
    if coverage_report and Path(coverage_report).exists():
        tree = ET.parse(coverage_report)
        root = tree.getroot()
        coverage_percentage = float(root.get("line-rate")) * 100
        if coverage_percentage < 80:
            for sourcefile in root.findall(".//class"):
                filename = sourcefile.get("filename")
                for line in sourcefile.findall(".//line[@hits='0']"):
                    uncovered_lines.append({"file": filename, "line": line.get("number")})
            issues.append({"type": "coverage", "percentage": coverage_percentage, "uncovered": uncovered_lines})
    
    return issues, coverage_percentage