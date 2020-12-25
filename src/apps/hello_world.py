"""Minimal Hello World Example"""
import panel as pn


def view():
    """Returns the app"""
    return pn.pane.Markdown("Hello World")


if __name__.startswith("bokeh"):
    view().servable()
