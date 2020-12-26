"""Minimal Hello World Example"""
import panel as pn


def view():
    """Returns the app"""
    return pn.pane.Markdown("# Hello World")


if __name__.startswith("bokeh"):
    # Run the development server
    # python -m panel serve 'src/apps/hello_world.py' --dev --show
    view().servable()
if __name__ == "__main__":
    # Run the server. Useful for integrated debugging in your Editor or IDE.
    # python 'src/apps/hello_world.py'
    view().show(port=5007)
