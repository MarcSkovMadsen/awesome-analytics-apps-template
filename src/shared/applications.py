"""Returns an example app using the OrstedGalleryTemplate"""
from src.shared.models import Application
from src.shared import persons
from src import config

GALLERY = Application(
    name="Gallery",
    introduction="An overview of all apps",
    description=(
        "The purpose of the Gallery is to enable to get inspiration and locate the app you " "need"
    ),
    author=persons.MARC_SKOV_MADSEN,
    url="gallery",
    thumbnail_url=config.THUMBNAILS_PREFIX + "gallery.png"
)
HOME = Application(
    name="Home",
    introduction="The landing page of the site",
    description=(
        "The landing page introduces the site and provides navigation"
    ),
    author=persons.MARC_SKOV_MADSEN,
    url="/",
    thumbnail_url=config.THUMBNAILS_PREFIX + "home.png"
)
HELLO_WORLD_FROM_FUNCTION = Application(
    name="Hello World from Function",
    introduction="A very simple Hello World app deployed from a FUNCTION",
    description=("A very simple Hello World app deployed from a function"),
    author=persons.MARC_SKOV_MADSEN,
    url="hello-world-from-function",
    thumbnail_url=config.THUMBNAILS_PREFIX + "hello_world.png"
)
HELLO_WORLD_FROM_PY_FILE = Application(
    name="Hello World from .py File",
    introduction="A very simple Hello World app deployed from a .py FILE",
    description=("A very simple Hello World app deployed from a .py file"),
    author=persons.MARC_SKOV_MADSEN,
    url="hello-world-from-file",
    thumbnail_url=config.THUMBNAILS_PREFIX + "hello_world.png"
)
HELLO_WORLD_FROM_NOTEBOOK = Application(
    name="Hello World from notebook File",
    introduction="A very simple Hello World app deployed from a NOTEBOOK",
    description=("A very simple Hello World app deployed from a notebook"),
    author=persons.MARC_SKOV_MADSEN,
    url="hello-world-from-notebook",
    thumbnail_url=config.THUMBNAILS_PREFIX + "hello_world.png"
)
HOLOVIEWS_LINKED_BRUSING = Application(
    url="holoviews-linked-brushing",
    name="HoloViews Linked Brushing",
    author=persons.MARC_SKOV_MADSEN,
    introduction="A demonstration of HoloViews linked brushing for Bokeh and Plotly backends",
    description=__doc__,
    thumbnail_url="holoviews-linked-brushing.png",
    code_url="holoviews_linked_brushing.py",
    mp4_url="holoviews-linked-brushing.mp4",
    tags=["Panel", "Bokeh", "Plotly", "HoloViews", "Linked Brushing", "Cross Filter"],
)
APPLICATIONS = [HOME, GALLERY, HELLO_WORLD_FROM_FUNCTION, HELLO_WORLD_FROM_NOTEBOOK, HELLO_WORLD_FROM_PY_FILE]