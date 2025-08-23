"""
Junk - Universal Cleanup Executor

A zero-friction Python CLI tool for automated cleanup of unwanted files.
This package provides a simple command-line interface for deleting files
and directories listed in a 'junk.fat' file.

Usage:
    1. Create a junk.fat file with files/folders to delete
    2. Run `junk` command
    3. Everything listed gets deleted, junk.fat self-destructs

Perfect for automated cleanup workflows.
"""

__version__ = "0.1.3"
__author__ = "Junk CLI"
__email__ = "maintainer@junk-cli.dev"
__description__ = "Universal cleanup executor - Automated deletion of unwanted files and directories"


from .cleanup import clean_up
from .cli import main

__all__ = ['clean_up', 'main', '__version__']
