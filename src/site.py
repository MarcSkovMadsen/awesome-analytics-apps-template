# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
"""In this module we provide functionality to launch our app"""
import os
import platform

import panel as pn

from src import config
from src.shared import modifications

from .routes import ROUTES

modifications.apply()


def run_server():
    address = os.getenv("BOKEH_ADDRESS", "localhost")
    if platform.system() == "Windows":
        pn.serve(
            ROUTES,
            port=5007,
            dev=False,
            title=config.SITE_NAME,
            address=address,
        )
    else:
        pn.serve(
            ROUTES,
            port=5007,
            dev=False,
            title=config.SITE_NAME,
            address=address,
            num_procs=4,
        )


if __name__ == "__main__":
    run_server()
