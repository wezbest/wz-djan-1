# These functions to be called in main
from rich.console import Console
from rich.markdown import Markdown
import subprocess
from rich import print as rprint


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


# Function to run the django server
def m2():
    # Run command
    p = subprocess.Popen(["uv", "run", "python", "panty1/manage.py", "runserver"])
    rprint("[magenta]Server started... press ctrl+c to stop[/magenta]")
    try:
        p.wait()
    except KeyboardInterrupt:
        p.terminate()
        rprint("""[red]
Server Stopped ..Fuck all nite ....[/red]""")
