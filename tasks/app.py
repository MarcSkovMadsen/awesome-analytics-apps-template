"""Module of Invoke tasks to run apps. Run

invoke --list=app

from the command line for a list of all available commands.
"""
from invoke import task

from src import site  # pylint: disable=import-outside-toplevel


@task(aliases=("panel",))
def run_server(
    _,
):
    """Starts the Panel server"""
    site.run_server()
