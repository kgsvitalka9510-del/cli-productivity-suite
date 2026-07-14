"""Project scaffolding tools."""

import click
import os
from pathlib import Path

TEMPLATES = {
    "api": {
        "description": "REST API with FastAPI",
        "files": {
            "main.py": '''"""FastAPI application."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
''',
            "requirements.txt": "fastapi\nuvicorn",
        }
    },
    "cli": {
        "description": "CLI tool with Click",
        "files": {
            "main.py": '''"""CLI application."""

import click

@click.command()
def main():
    click.echo("Hello World")

if __name__ == "__main__":
    main()
''',
            "requirements.txt": "click",
        }
    },
    "web": {
        "description": "Web app with Flask",
        "files": {
            "app.py": '''"""Flask application."""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
''',
            "requirements.txt": "flask",
        }
    }
}

@click.group()
def scaffold_group():
    """Project scaffolding."""
    pass

@scaffold_group.command()
@click.option("--template", "-t", type=click.Choice(list(TEMPLATES.keys())), required=True)
@click.option("--name", "-n", required=True, help="Project name")
@click.option("--path", "-p", default=".", help="Output path")
def create(template, name, path):
    """Create project from template."""
    if template not in TEMPLATES:
        click.echo(f"Unknown template: {template}")
        return
    
    project_dir = os.path.join(path, name)
    os.makedirs(project_dir, exist_ok=True)
    
    tmpl = TEMPLATES[template]
    for filename, content in tmpl["files"].items():
        filepath = os.path.join(project_dir, filename)
        with open(filepath, "w") as f:
            f.write(content)
        click.echo(f"Created {filepath}")
    
    click.echo(f"\nProject created: {name}")
    click.echo(f"Template: {tmpl['description']}")

@scaffold_group.command()
def list_templates():
    """List available templates."""
    click.echo("Available templates:\n")
    for name, tmpl in TEMPLATES.items():
        click.echo(f"  {name:10s} - {tmpl['description']}")
