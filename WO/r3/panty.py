from rich.console import Console
from rich.markdown import Markdown
import subprocess


def main():
    m1()


# Rendering Markup Function


def m1():
    subprocess.run(["clear"])
    MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item

# To Run the server 

```py 
uv run python manage.py runserver
```

"""

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)


if __name__ == "__main__":
    main()
