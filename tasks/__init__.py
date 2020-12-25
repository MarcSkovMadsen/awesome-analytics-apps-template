"""Here we import the different task submodules/ collections"""
from invoke import Collection

from . import app, docker, test

# pylint: disable=invalid-name
# as invoke only recognizes lower case
namespace = Collection()
namespace.add_collection(app)
namespace.add_collection(docker)
namespace.add_collection(test)
