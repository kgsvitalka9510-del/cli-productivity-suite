"""CLI Productivity Suite - Main Entry Point."""

import click
from git_tools import git_group
from review import review_group
from scaffold import scaffold_group

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """CLI Productivity Suite - Professional tools for developers."""
    pass

cli.add_command(git_group, "git-tools")
cli.add_command(review_group, "review")
cli.add_command(scaffold_group, "scaffold")

if __name__ == "__main__":
    cli()
