import openai

class OpenRouterClient:
    """OpenRouter API client using OpenAI-compatible SDK (>=1.0.0)."""
    def __init__(self):
        self.client = openai.OpenAI(
            api_key="API-KEY",
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
            return response.choices[0].message.content
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
Return the test code in a single block.
"""
    return openrouter_client.generate(prompt)
