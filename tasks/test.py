"""Module of Invoke TEST TASKS to be invoked from the command line. Try

invoke --list==test

from the command line for a list of all available commands.
"""

import os
import pathlib

from invoke import task

TEST_FILES = " ".join(
    [
        "tests",
        "src/apps",
    ]
)
TEST_RESULTS = "test_results"
FILES = " ".join(
    [
        "src",
        "tasks",
        "tests",
    ]
)


@task
def bandit(
    command,
):
    """Runs Bandit the security linter from PyCQA."""
    print(
        """
Running Bandit the Python Security Linter
to identify common security issues in Python code
=================================================
"""
    )
    command.run(
        "bandit -r ./",
        echo=True,
    )


@task
def black(
    command,
):
    """Runs black (autoformatter) on all .py files recursively"""
    print(
        """
Running Black the Python code formatter
=======================================
"""
    )
    command.run(
        "black .",
        echo=True,
    )


@task
def isort(
    command,
):
    """Runs isort (import sorter) on all .py files recursively"""
    print(
        """
Running isort the Python code import sorter
===========================================
"""
    )
    command.run(
        "isort .",
        echo=True,
    )


@task
def pytest(
    command,
    test_files=TEST_FILES,
    test_results=False,
    skip_integrationtest=False,
    show=False,
):
    """Runs pytest to identify failing tests

    Arguments:
        command {[type]} -- Invoke command object

    Keyword Arguments:
        root_dir {str} -- The directory from which to run the tests
        test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
        test_results {string} -- If set test reports will be generated in the
            test_results folder
        skip_integrationtest {bool} -- Whether or not to run tests marked integrationtest.
            In the CI/ CD pipeline this is nescessary is there is no connection to the database.
        show {bool} -- If True then the code coverage report will be shown when the test is done.

    # Print running pytest
    """
    print(
        """
Running pytest the test framework
=================================
"""
    )
    # Build the command_string
    command_string = f"pytest {test_files} --doctest-modules"
    if skip_integrationtest:
        command_string += ' -m "not integrationtest"'

    if test_results or show:
        command_string += " --junitxml=test_results/pytest-results.xml"
        command_string += " --cov=src --cov-report html:test_results/cov_html"
        command_string += " --cov-report xml:test_results/coverage.xml"

    # Run the command_string
    command.run(
        command_string,
        echo=True,
    )

    # Open the test coverage report in a browser
    if show:
        _show_coverage()
    if test_results:
        print("""- generated test coverage file at test_results/cov_html/index.html""")


def _show_coverage():
    path = pathlib.Path(__file__).parent.parent / "test_results" / "cov_html" / "index.html"
    os.system(f"start {str(path)}")


@task()
def show_coverage(_):
    """Open the code coverage report in a browser"""
    _show_coverage()


@task()
def pylint(command, files=FILES, test_results=False):
    """Runs pylint (linter) on all .py files recursively to identify coding errors

    Arguments:
        command {[type]} -- [description]
        files {string} -- A space separated list of files and folders to lint
        test-results {bool} -- If set then the test_results/pylint report will be generated
    """
    print(
        """
Running pylint.
Pylint looks for programming errors, helps enforcing a coding standard,
sniffs for code smells and offers simple refactoring suggestions.
=======================================================================
"""
    )
    command_string = f"pylint {files}"
    if test_results:
        if not os.path.exists("test_results"):
            os.makedirs("test_results")
        command_string += (
            " --output-format=pylint2junit.JunitReporter 2>&1 > test_results/pylint-results.xml"
        )

    command.run(
        command_string,
        echo=True,
    )


@task
def mypy(command, files=FILES, test_results=False):
    """Runs mypy (static type checker) on all .py files recursively

    Arguments:
        command {[type]} -- [description]
        files {string} -- A space separated list of files and folders to lint
        test-results {bool} -- If set then then the test_results/mypy-results.xml report will
            be generated
    """
    print(
        """
Running mypy for identifying Python type errors
===============================================
"""
    )
    command_string = f"mypy {files}"
    if test_results:
        command_string += " --junit-xml test_results/mypy-results.xml"
    command.run(
        command_string,
        echo=True,
    )


@task
def autoflake(
    command,
):
    """Runs autoflake to remove unused imports on all .py files recursively

    Arguments:
        command {[type]} -- [description]
    """
    print(
        """
Running autoflake to remove unused imports on all .py files recursively
=======================================================================
"""
    )
    # command.run("RUN rm -rf .mypy_cache/; exit 0")
    command.run(
        "autoflake --imports=pytest --in-place --recursive .",
        echo=True,
    )


@task(
    pre=[
        isort,
        autoflake,
        black,
        pylint,
        mypy,
        pytest,
    ],
    name="all",
)
def _all(
    command,
):  # pylint: disable=unused-argument
    """Runs isort, autoflake, black, pylint, mypy and pytest

    Shows the code coverage report when successfull

    Arguments:
        command {[type]} -- [description]
    """
    # If we get to this point all tests listed in 'pre' have passed
    # unless we have run the task with the --warn flag
    if not command.config.run.warn:
        print(
            """
All Tests Passed Successfully
=============================
"""
        )
