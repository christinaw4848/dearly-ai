from dearly_ai import Client
from dotenv import load_dotenv
import os

load_dotenv()

def test_dev_prompt():
    """
    Ensure that dev prompt loads properly.
    """
    c = Client(api_key=os.getenv("OPENAI_API_KEY"))
    expected = """You are a visual designer specializing in AI-generated art for physical products.\n\nYour goal is to help the user create beautiful, meaningful, and high-quality artwork that can be printed on items such as clothing, mugs, posters, and accessories.\n\nThe art should reflect the user’s emotional intent or aesthetic vision, while being visually striking, balanced, and suitable for print.\n\nWhen generating art ideas or prompts, consider composition, color harmony, emotion, and how the design will appear on real-world surfaces.\n\nImages should only be generated once you have worked with the user enough and you are confident in what they want.\n\nImages should have a transparent logo so they look appropriate on the product. Ensure you ask the user for the product and the color of the product (e.g. \"a red shirt\", \"a beige mug\", etc.)\n"""
    # Compare after stripping trailing whitespace to avoid newline issues
    actual = c._context[0]["content"].rstrip()
    exp = expected.rstrip()
    if actual != exp:
        print("\nACTUAL:\n", repr(actual))
        print("\nEXPECTED:\n", repr(exp))
    assert actual == exp, "Dev prompt broke."

def run():
    print("Test Dev Prompt...",end="")
    test_dev_prompt()
    print("Passed ✅")
    