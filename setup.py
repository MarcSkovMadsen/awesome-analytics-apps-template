"""Setup file for the Site"""

import setuptools

install_requires = [
    "awesome-panel-extensions==20201221.1",  # Templates etc.
]

_apps = [
    "pandas==1.1.5",
    "holoviews==1.14.0",
    "hvplot==0.7.0",
    "plotly==4.14.1",
    "altair==4.1.0",
    "streamz==0.6.1",
    "bqplot=0.12.19",
    "ipyleaflet=0.13.3",
    "ipywidgets=7.6.1",
    "gpxpy=1.4.2",
    "srtm.py=0.3.6",
    "ipywidgets_bokeh==1.0.2",  # To enable using IPyWidgets
]
_jupyter = [
    # For working in jupyter notebook or jupyter lab
    "notebook==6.1.5",
    "jupyterlab==2.2.9",  # pyviz/jupyterlab_pyviz does not yet support 3.0
    "jupyter_contrib_nbextensions==0.5.1",  # To enable cleaning jupyter notebooks
]
_tests = [
    # Utils
    # ------------------------------------------------------------------------------
    "invoke==1.4.1",  # Invoke is a Python task execution tool & library. See http://www.pyinvoke.org/
    # Testing
    # ------------------------------------------------------------------------------
    "pytest==6.2.1",  # The pytest framework makes it easy to write tests. See https://github.com/pytest-dev/pytest
    "pytest-cov==2.10.1",  # Test coverage. See https://pypi.org/project/pytest-cov/
    # Code quality
    # ------------------------------------------------------------------------------
    "isort==5.6.4",  # Sort import statements. We need 4.3.15 to correctly sort dataclasses
    "pylint==2.6.0",  # Linter.
    "pylint2junit==1.0.1",  # Used to generate junit xml reports in azure pipelines https://pypi.org/project/pylint2junit/
    "black==20.8b1",  # Auto formatter.
    "autoflake==1.4",  # Automatically removes unused imports and unused variables. See https://github.com/myint/autoflake
    "coverage==5.3",  # https://github.com/nedbat/coveragepy
    "mypy==0.790",  # https://github.com/python/mypy
    "bandit==1.7.0",  # Bandit is a tool designed to find common security issues in Python code. See https://pypi.org/project/bandit/
]

extras_require = {
    "apps": _apps,
    "jupyter": _jupyter,
    "tests": _tests,
}

extras_require["all"] = sorted(set(sum(extras_require.values(), [])))

setuptools.setup(
    name="awesome-analytics-apps-template",
    version="20201227.1",
    description="""The Awesome Analytics Apps Template makes it easy to start a site similar to
awesome-panel.org""",
    long_description="""The Awesome Analytics Apps Template makes it easy to start a site similar to
awesome-panel.org""",
    long_description_content_type="text/markdown",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    platforms=["Windows", "Mac OS X", "Linux"],
    license="Apache Software License",
    url="https://github.com/marcskovmadsen/awesome-analytics-apps-starter",
    # My Project contains more folders/ packages but they should not be included
    packages=setuptools.find_packages(include=["src", "src.*"]),
    include_package_data=True,
    classifiers=[
        # I would like to indicate that this package is a package for the Panel framework
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require["tests"],
)
