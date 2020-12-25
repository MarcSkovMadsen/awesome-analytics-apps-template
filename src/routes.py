"""Provides the ROUTES of the site"""
import pathlib

from src.apps import hello_world, linked_selections

_APPS_ROOT = pathlib.Path(__file__).parent / "apps"

ROUTES = {
    "hello-world-file": _APPS_ROOT / "hello_world.py",
    "hello-world": hello_world.view,
    "hello-world-notebook": _APPS_ROOT / "hello_world.ipynb",
    "linked-selections": linked_selections.view,
    "linked-selections-notebook": _APPS_ROOT / "notebook_example.ipynb",
}
