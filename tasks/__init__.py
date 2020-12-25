"""Here we import the different task submodules/ collections"""
from invoke import Collection

from . import docker, site, test

# pylint: disable=invalid-name
# as invoke only recognizes lower case
namespace = Collection()
namespace.add_collection(site)
namespace.add_collection(docker)
namespace.add_collection(test)
