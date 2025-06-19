import os
from test_generator import openrouter_client

def refine_tests(test_file,src_file, issues):
    """Refine test cases based on issues."""
    with open(test_file, "r", encoding="utf-8") as f:
        test_code = f.read()
    
    issue_summary = "\n".join(
        f"{'Failure: ' + str(issue['details']) if issue['type'] == 'failure' else 'Uncovered lines: ' + str(issue['uncovered'])}"
        for issue in issues
    )
    
    prompt = f"""
For the below Python source file:

```python
{src_file}
```

The following test cases are written which has issues:

```python
{test_code}
```

Issues:
{issue_summary}

Only Modify the test case which is causing the issue , fix failures and cover uncovered lines.
Generate **only** `pytest` test cases
For importing function and classes use src as root folder for example from src import module
Return the updated test code in a single block wrapped in ```python ... ```.
"""
    try:
        new_test_code = openrouter_client.generate(prompt)
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(new_test_code)
        return new_test_code
    except Exception as e:
        raise RuntimeError(f"Test refinement failed: {str(e)}")