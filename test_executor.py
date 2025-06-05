import subprocess
from pathlib import Path
import os

def run_tests():
    """Run pytest with coverage and return results."""
    env = os.environ.copy()
    env["PYTHONPATH"] = "src" 
    result = subprocess.run(
        ["pytest", "--cov=src", "--cov-report=xml", "tests/"],
        capture_output=True,
        text=True
    )
    coverage_report = Path("my-python-project/coverage.xml")
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "coverage_report": str(coverage_report) if coverage_report.exists() else None
    }