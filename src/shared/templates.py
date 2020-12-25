"""Provides customized and branded versions of the templates to be used in the site"""
# This will make it much easier to customize your templates when you start wanting to brand your
# site.
import param
from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate as _FastGalleryTemplate,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_grid_template import (
    FastGridTemplate as _FastGridTemplate,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_template import (
    FastTemplate as _FastTemplate,
)

from src.config import SITE_NAME


class ListTemplate(_FastTemplate):
    __doc__ = _FastTemplate.__doc__

    site = param.String(SITE_NAME)


class GridTemplate(_FastGridTemplate):
    __doc__ = _FastGridTemplate.__doc__

    site = param.String(SITE_NAME)


class GalleryTemplate(_FastGalleryTemplate):
    __doc__ = _FastGalleryTemplate.__doc__

    site = param.String(SITE_NAME)
