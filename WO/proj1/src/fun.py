# Functions to run the server from panty.py

from rich import print as rprint
from rich.markdown import Markdown
from rich.console import Console

console = Console()


# markdown Function
def markdown1():
    MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)
