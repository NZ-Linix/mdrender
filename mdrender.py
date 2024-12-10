#!/usr/bin/env python3

from rich.console import Console
from rich.markdown import Markdown
from rich import print as p
import sys, os

console = Console()

def mdrender(mdfile):
    try:
        with open(mdfile, 'r') as f:
            markdown = Markdown(f.read())
    except Exception as e:
        print()
        p(f"[bold red]Error reading file:[/]\n {e}")
        print()
        sys.exit(1)

    try:
        print()
        print()
        console.print(markdown)
        print()
        print()
    except Exception as e:
        print()
        p(f"[bold red]Error rendering markdown:[/]\n {e}")
        print()
        sys.exit(1)

if len(sys.argv) < 2:
    print()
    p("[bold red]Usage: mdrender <markdown file>[/]")
    print()
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print()
    p(f"[bold red]File {sys.argv[1]} not found[/]")
    print()
    sys.exit(1)

if sys.argv[1][-2:] != 'md':
    print()
    p(f"[bold red]File {sys.argv[1]} is not a markdown file[/]")
    print()
    sys.exit(1)

mdrender(sys.argv[1])