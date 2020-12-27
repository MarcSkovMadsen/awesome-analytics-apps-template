"""Module of Invoke tasks to be invoked from the command line. Try

invoke --list=docker

from the command line for a list of all available commands.
"""
import os
import pathlib
import subprocess
from dataclasses import dataclass
from typing import List, Union

import toml

# pylint: disable=invalid-name
# because Invoke uses 'c' for the Invoke command object
from invoke import task

REGISTRY = "registry.hub.docker.com"
IMAGE_BASE = "base"
IMAGE_PROD = "prod"
IMAGE_TEST = "test"


def read_config_from_toml(path: Union[str, pathlib.Path]):
    """Reads the configuration from a .toml file. For example pyproject.toml"""
    if isinstance(path, str):
        path = pathlib.Path(path)
    config = toml.load(path)

    if "docker" in config:
        config = config["docker"]
        # pylint: disable=global-statement
        global REGISTRY, IMAGE_BASE, IMAGE_PROD, IMAGE_TEST, IMAGES
        REGISTRY = config.get("registry", REGISTRY)
        IMAGE_BASE = config.get("image_base", IMAGE_BASE)
        IMAGE_PROD = config.get("image_prod", IMAGE_PROD)
        IMAGE_TEST = config.get("image_test", IMAGE_TEST)
        IMAGES = _get_images()


def _build(  # pylint: disable=too-many-arguments
    c, docker_file: str, image: str, tag: str, context: str, rebuild: bool = False
):
    """Helper function for docker build

    Arguments:
        c {[type]} -- Invoke command object
        docker_file {str} -- The path to the Docker file
        image {str} -- The name of the Docker image
        tag {str} -- The Docker tag
        context {str} -- The context to use for building the Docker image
        rebuild {bool} - If true we rebuild from scratch
    """
    print(
        f"""
Building the '{image}:{tag}' Docker image
"""
    )
    if rebuild:
        command = (
            f"docker build --no-cache --rm -f {docker_file} -t {image}:{tag} -t {image}:latest "
        )
    else:
        command = f"docker build --rm -f {docker_file} -t {image}:{tag} -t {image}:latest "

    build_args: List[str] = []
    for arg in build_args:
        value = os.getenv(arg)
        if value:
            command += f" --build-arg {arg}={value}"

    command = command + " " + context

    if build_args:
        c.run(command, echo=True)  # Do not echo secrets
    else:
        c.run(command, echo=True)


@dataclass
class Image:
    """Model of Docker Image. Used to hold settings"""

    name: str
    docker_file: str
    context: str
    dependencies: List
    registry: str

    @property
    def image(self) -> str:
        """The full name of the image, i.e. registry/name

        Returns:
            str -- The full name of the image
        """

        return f"{self.registry}/{self.name}"

    def to_image(self, registry: str) -> str:
        """Returns the registry/name

        Args:
            registry (str): The name of the registry. For example datalakek8sacrdev.azurecr.io

        Returns:
            str: For example datalakek8sacrdev.azurecr.io/trading-analytics/backend-pre
        """
        return f"{registry}/{self.name}"


def _get_images():
    return {
        "base": Image(
            docker_file="devops/docker/Dockerfile.base",
            name=IMAGE_BASE,
            context="requirements",
            dependencies=[],
            registry=REGISTRY,
        ),
        "prod": Image(
            docker_file="devops/docker/Dockerfile.prod",
            name=IMAGE_PROD,
            context=".",
            dependencies=["base"],
            registry=REGISTRY,
        ),
        "test": Image(
            docker_file="devops/docker/Dockerfile.test",
            name=IMAGE_TEST,
            context=".",
            dependencies=["prod"],
            registry=REGISTRY,
        ),
    }


IMAGES = _get_images()


@task
def build(c, image="prod", tag="latest", registry=REGISTRY, rebuild=False):
    """Build Docker image

    Arguments:
        c {[type]} -- Invoke command

    Keyword Arguments:
        image {str} -- Image name: base, prod or test (default: {"prod"})
        tag {str} -- Image tag.
            If tag != "latest" then the image will be tagged with both tag and 'latest' (default: {"latest"})
        rebuild {bool} -- If set then the image and all dependencies are rebuilt from scratch (default: {False})
    """
    image_configuration = IMAGES.get(image, IMAGES["prod"])  # We use the backend image by default

    if rebuild:
        for dependent_image in image_configuration.dependencies:
            build(c, image=dependent_image, tag=tag, registry=registry, rebuild=rebuild)

    _build(
        c,
        docker_file=image_configuration.docker_file,
        image=image_configuration.to_image(registry=registry),
        tag=tag,
        context=image_configuration.context,
        rebuild=False,
    )


@task
def run(c, image="prod", tag="latest", config_file=""):  # pylint: disable=unused-argument
    """Run the (prod) Docker image interactively.

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- Either prod, base or test (default: {"prod"})
        tag {str} -- Name of tag (default: {"latest"})
    """

    # Invoke cannot run interactive
    print(
        f"""
Running the '{image}:{tag}' Docker image
========================================
"""
    )
    image_configuration = IMAGES.get(image, IMAGES["prod"])  # We use the backend image by default

    if config_file:
        command = (
            f"docker run --env CONFIG_FILE={config_file} -p 5007:5007 "
            f"-it {image_configuration.registry}/{image_configuration.name}:{tag}"
        )
    else:
        command = (
            f"docker run -p 5007:5007 "
            f"-it {image_configuration.registry}/{image_configuration.name}:{tag}"
        )
    print(command)
    subprocess.run(command, check=True)


@task()
def serve(c, image="prod", tag="latest"):  # pylint: disable=unused-argument
    """Start the serve and serve the apps.

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- Either prod, base or test (default: {"prod"})
        tag {str} -- Name of tag (default: {"latest"})
    """

    # Invoke cannot run interactive
    print(
        f"""
Running the '{image}:{tag}' Docker image
========================================
"""
    )
    image_configuration = IMAGES.get(image, IMAGES["prod"])
    command = (
        f"docker run -it -p 5007:5007 --entrypoint python "
        f"{image_configuration.registry}/{image_configuration.name}:{tag} src/site.py"
    )
    print(command)
    subprocess.run(command, check=True)


@task
def export_test_results(c):
    """Copies the test_results from the test image to the local folder 'test_results'"""
    print(
        """
Copying the test_results from the test image to the local folder 'test_results'
===================================================================================
"""
    )
    result = c.run(
        "docker create datalakek8sacrdev.azurecr.io/trading-analytics/package_test:latest",
        echo=True,
    )
    container_id = result.stdout.replace("\n", "")

    c.run(f"docker cp {container_id}:/app/test_results/. test_results", echo=True)
    c.run(f"docker rm -v {container_id}", echo=True)
    c.run("ls test_results", echo=True)


@task(post=[export_test_results])
def test(c, rebuild=False):
    """Run the pre-commit tests inside the docker container

    This will
    1. Rebuild prod and test using cache
    2. Run tests using isort, black, pylint, mypy and pytest.
        This is the same as the tests in Azure Pipelines and as the the command 'invoke code.all'
        The test results are available in the test container in the /app/test_results folder and
            in the local ./test_results folder
        The test results are in the junit format so that they can be published and inspected in Azure Devops.

    Arguments:
        c {[type]} -- [description]

    Keyword Arguments:
        rebuild {bool} -- If set then the image and all dependencies are rebuilt from scratch (default: {False})
    """
    if rebuild:  # rebuild all images
        build(c, image="test", rebuild=True)
    else:  # speed up using caching
        build(c, image="prod")
        build(c, image="test")


@task
def system_prune(c):
    """The docker system prune command will free up space

    It removes all stopped containers, all dangling images, and
    all unused networks to free up space.

    See https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/
    """
    print(
        """Cleaning up the Docker system
================================
"""
    )
    c.run("docker system prune", echo=True)
