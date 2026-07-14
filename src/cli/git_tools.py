"""Git workflow automation tools."""

import click
import subprocess
from datetime import datetime

@click.group()
def git_group():
    """Git workflow automation."""
    pass

@git_group.command()
@click.option("--files", "-f", multiple=True, help="Files to stage")
def smart_commit(files):
    """Auto-generate commit message from changes."""
    if not files:
        # Get changed files
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            capture_output=True, text=True
        )
        files = result.stdout.strip().split("\n")
    
    # Analyze changes
    changes = []
    for f in files:
        if f.endswith(".py"):
            changes.append(f"Update {f}")
        elif f.endswith(".md"):
            changes.append(f"Update docs: {f}")
        else:
            changes.append(f"Update {f}")
    
    message = ", ".join(changes) if changes else "Minor updates"
    click.echo(f"Commit message: {message}")
    
    if click.confirm("Create commit?"):
        subprocess.run(["git", "add"] + list(files))
        subprocess.run(["git", "commit", "-m", message])
        click.echo("Committed!")

@git_group.command()
@click.option("--title", "-t", help="PR title")
@click.option("--body", "-b", help="PR description")
def pr_create(title, body):
    """Create pull request with description."""
    if not title:
        title = click.prompt("PR title")
    if not body:
        body = click.prompt("PR description")
    
    # Create PR using gh CLI
    cmd = ["gh", "pr", "create", "--title", title, "--body", body]
    subprocess.run(cmd)
    click.echo("PR created!")
