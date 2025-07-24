# Dearly AI

A library to easily use generative AI tools.

## Setup

1. `git clone https://github.com/leekycauldron/dearly-ai.git`
2. `cd dearly-ai`
3. `pip install -e .`
4. Set `OPENAI_API_KEY` in `.env.example` and rename file to `.env`

## Usage

Check examples for usage, docs coming soon.
`import dearly_ai`

## Example

Here's how to use Dearly AI to generate an image and get model outputs:

```python
from dearly_ai import Client

client = Client(api_key="YOUR_OPENAI_API_KEY")

# Generate an image from a prompt
result = client.response("I want a cartoon cat design")
print(result)  # This will print the assistant's message, including an <img> tag
```

### Model Output Format
- The response is a string containing HTML, e.g.:
  - Text: "[Image generated: output.png]"
  - Image: `<img src="data:image/png;base64,..." alt="Generated Image">`
- If you want the raw output as a Python object, you can inspect the context:
  - Each message in `client._context` is a dict: `{ 'role': 'user'|'assistant', 'content': str }`
  - Image is returned as a base64-encoded string inside the `<img>` tag (not bytes or URL)

### Example Output
```json
[
  {
    "role": "assistant",
    "content": "[Image generated: output.png]<br><img src=\"data:image/png;base64,...\" alt=\"Generated Image\">"
  }
]
```
