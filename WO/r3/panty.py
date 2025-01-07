from rich.console import Console
from rich.markdown import Markdown
import subprocess
from rich.traceback import install

install(show_locals=True)


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

# To Run the server - Server will staert with this command

```py 
uv run python manage.py runserver
```

# Now the server will be started with the command 

"""

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

    # Run command
    subprocess.run(["uv", "run", "python", "panty1/manage.py", "runserver"])


if __name__ == "__main__":
    main()
