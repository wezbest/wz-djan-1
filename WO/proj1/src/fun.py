# Functions to run the server from panty.py

from rich import print as rprint
from rich.markdown import Markdown
from rich.console import Console
from rich.traceback import install
import subprocess

install(show_locals=True)
console = Console()


# markdown Function
def markdown1():
    subprocess.run(["clear"])
    MARKDOWN = """
# Executing Server Script 

```py 
uv run manage.py runserver
```
"""
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)


def run_server():
    # Run command
    p = subprocess.Popen(["uv", "run", "python", "worldtour/manage.py", "runserver"])
    rprint("""[bold green]
----           
Server started... press ctrl+c to stop
------[/bold green]""")
    try:
        p.wait()
    except KeyboardInterrupt:
        p.terminate()
        rprint("""[red]
Server Stopped ..Fuck all nite ....[/red]""")
