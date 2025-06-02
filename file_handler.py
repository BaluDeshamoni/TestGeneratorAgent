import os
from pathlib import Path

def scan_files(directory):
    """Scan directory for .py files, excluding tests."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py") and "tests" not in root and not filename.startswith("test_"):
                file_path = Path(root) / filename
                with open(file_path, "r", encoding="utf-8") as f:
                    files.append({"path": str(file_path), "content": f.read()})
    return files

def save_tests(test_code, source_path):
    """Save test code to tests/ directory."""
    test_dir = Path("my-python-project/tests")
    test_dir.mkdir(exist_ok=True)
    test_filename = "test_" + Path(source_path).name
    test_path = test_dir / test_filename
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(test_code)
    return str(test_path)