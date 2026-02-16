class Assistant:
    """
    A simple assistant class for the Axynn Assistant project.
    """
    def __init__(self, name="Axynn"):
        self.name = name

    def greet(self, user_name="User"):
        """Returns a greeting message."""
        return f"Hello, {user_name}! I am {self.name}, your assistant."
