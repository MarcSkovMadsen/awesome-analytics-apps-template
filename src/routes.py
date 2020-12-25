"""Provides the ROUTES of the site"""
import pathlib

from src.apps import home, gallery, hello_world, linked_selections

_APPS_ROOT = pathlib.Path(__file__).parent / "apps"
ROUTES = {
    "": home.view,
    "hello-world-from-function": hello_world.view,
    "hello-world-from-file": _APPS_ROOT / "hello_world.py",
    "hello-world-from-notebook": _APPS_ROOT / "hello_world.ipynb",
    "gallery": gallery.view,
    "linked-selections": linked_selections.view,
    "linked-selections-notebook": _APPS_ROOT / "notebook_example.ipynb",
}
