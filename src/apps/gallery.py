from src.shared.templates import GalleryTemplate
from src.shared.applications import APPLICATIONS


def view():
    return GalleryTemplate(resources=APPLICATIONS)


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show(port=5007)
