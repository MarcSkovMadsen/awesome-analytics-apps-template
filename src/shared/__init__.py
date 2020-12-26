"""Provides

- config: An instance of SiteConfig holding the current Site configuration
"""
import pathlib

from ._config import _create_site_config

CONFIG_ROOT = pathlib.Path(__file__).parent.parent / "config"

config = _create_site_config(config_root=CONFIG_ROOT)
