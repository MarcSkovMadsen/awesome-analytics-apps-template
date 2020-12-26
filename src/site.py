# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
"""In this module we provide functionality to launch our app"""
import os
import platform

import panel as pn

from src.shared import config, modifications

modifications.apply()


def serve():
    address = os.getenv("BOKEH_ADDRESS", "localhost")
    if platform.system() == "Windows":
        pn.serve(
            config.routes,
            port=5007,
            dev=False,
            title=config.site_name,
            address=address,
            static_dirs=config.static_dirs,
        )
    else:
        pn.serve(
            config.routes,
            port=5007,
            dev=False,
            title=config.site_name,
            address=address,
            num_procs=4,
            static_dirs=config.static_dirs,
        )


if __name__ == "__main__":
    serve()
