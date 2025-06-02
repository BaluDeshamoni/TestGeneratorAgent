import subprocess
from pathlib import Path

def run_tests():
    """Run pytest with coverage and return results."""
    result = subprocess.run(
        ["pytest", "--cov=src", "--cov-report=xml", "tests/"],
        capture_output=True,
        text=True
    )
    coverage_report = Path("coverage.xml")
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "coverage_report": str(coverage_report) if coverage_report.exists() else None
    }