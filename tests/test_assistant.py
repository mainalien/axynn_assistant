import sys
import os
import pytest

# Add the src directory to the system path so we can import the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from assistant import Assistant

def test_assistant_default_name():
    """Test that the assistant has the default name 'Axynn'."""
    assistant = Assistant()
    assert assistant.name == "Axynn"

def test_assistant_custom_name():
    """Test that the assistant can be initialized with a custom name."""
    assistant = Assistant("Helper")
    assert assistant.name == "Helper"

def test_greet_default():
    """Test the greet method with a default user name."""
    assistant = Assistant()
    assert assistant.greet() == "Hello, User! I am Axynn, your assistant."

def test_greet_custom():
    """Test the greet method with a custom user name."""
    assistant = Assistant()
    assert assistant.greet("Alice") == "Hello, Alice! I am Axynn, your assistant."
