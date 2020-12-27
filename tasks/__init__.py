"""Here we configure the cli tasks available via `invoke <namespace>.<command>`"""
from invoke import Collection

from . import docker, notebook, site, test

docker.read_config_from_toml("pyproject.toml")

# pylint: disable=invalid-name
# as invoke only recognizes lower case
namespace = Collection()
namespace.add_collection(site)
namespace.add_collection(docker)
namespace.add_collection(notebook)
namespace.add_collection(test)
