import openai
import re

class OpenRouterClient:
    """OpenRouter API client using OpenAI-compatible SDK (>=1.0.0)."""
    def __init__(self):
        self.client = openai.OpenAI(
            api_key="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",
            base_url="https://openrouter.ai/api/v1"
        )

    def generate(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",  # Or any other OpenRouter-supported model
                messages=[
                    {"role": "system", "content": "You are a skilled Python developer specializing in pytest unit tests."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000
            )
            # Extract only the Python code block from the response
            content = response.choices[0].message.content
            # Use regex to find code between ```python and ```
            match = re.search(r'```python\n(.*?)\n```', content, re.DOTALL)
            if match:
                return match.group(1).strip()
            else:
                raise ValueError("No Python code block found in API response")
        except Exception as e:
            raise RuntimeError(f"OpenRouter API error: {str(e)}")


openrouter_client = OpenRouterClient()

def generate_tests(file_content):
    """Generate pytest test cases for a Python file."""
    prompt = f"""
Given the following Python code:

```python
{file_content}
```

Generate pytest test cases to achieve at least 80% code coverage. Include:
- Tests for all functions and classes.
- Mock dependencies using unittest.mock.
- Handle edge cases and exceptions.
Return the test code in a single block wrapped in ```python ... ```.
"""
    return openrouter_client.generate(prompt)