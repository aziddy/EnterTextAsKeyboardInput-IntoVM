"""ANSI color codes for console output."""

# Basic colors
RED = '\033[91m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

# Text styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
DIM = '\033[2m'

# Reset
RESET = '\033[0m'

# def colorize(text, color):
#     """Wrap text in color codes."""
#     return f"{color}{text}{RESET}"

# # Convenience functions for common operations
# def error(text):
#     """Format text as an error message."""
#     return colorize(f"Error: {text}", RED)

# def success(text):
#     """Format text as a success message."""
#     return colorize(text, GREEN)

# def warning(text):
#     """Format text as a warning message."""
#     return colorize(text, ORANGE) 