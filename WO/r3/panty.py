from rich.console import Console
from rich.markdown import Markdown


def main():
    print("Hello from r3!")


# Rendering Markup Function

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""


console = Console()
md = Markdown(MARKDOWN)
console.print(md)


if __name__ == "__main__":
    main()
