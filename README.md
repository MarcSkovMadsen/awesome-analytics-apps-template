# Awesome Panel Starter

The purpose of this project is to enable you quickly get up and running building your own
site using Panel similarly to awesome-panel.org.

## Prerequisites

- Python >= 3.7 from [python.org](https://www.python.org/) installed.
- A recent version of [pip](https://pypi.org/project/pip/).
- An editor like VS Code (recommended for DevOps), PyCharm (very good editor for Python), Spyder or similar.

## Installation

Below we will describe

- installation via pip or conda.
- how to test the installation
- how to start the panel server

### Install Using Pip

Move to the **root of the project**. Create a virtual environment named **.venv**.

```bash
python -m venv .venv
```

Activate the virtual environment using something like `source .venv/Scripts/activate` (bash) or `.venv/Scrips/activate` (cmd.exe).

Update pip

```bash
python -m pip install --upgrade pip
```

Install the requirements for local development and testing.

```bash
pip install -r requirements/local.txt
```

## Install using Conda

COMING UP

## Test the installation

Test the installation by running the command

```bash
invoke test.all
```

## Start the Server


## Development and Testing

### The Command Line Interface (CLI)

We use [Invoke](http://docs.pyinvoke.org/) as a cli/ task runner to speed up our work flow. Tasks are defined in the `task` module. Available tasks can be listed using the `--list` flag and more information can be obtained using the `--help` flag.

```bash
$ invoke --list
Available tasks:

  test.all (test.pre-commit, test.test)   Runs isort, black pylint, mypy and pytest
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
  docker.build                            Build Docker image
  docker.export-test-results              Copies the test_results from the api_test image to the local folder 'test_results'
  docker.run                              Run the (api) Docker image interactively.
  docker.test                             Run the pre-commit tests inside the docker container
```

## Code Quality

To ensure a high coding standard we use

- [Autoflake](https://github.com/myint/autoflake): Automatically removes unused imports and unused variables
- [Isort](https://pypi.org/project/isort/): Isort your python imports for you so you don’t have to.
- [Black](https://github.com/ambv/black): Black is the uncompromising Python code formatter
- [Pylint](https://www.pylint.org/): Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells.
- [MyPy](http://mypy-lang.org/index.html): MyPy is a static type checker for Python
- [Pytest](https://docs.pytest.org/en/latest/): The pytest framework makes it easy to write tests
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/): Coverage.py is a tool for measuring code coverage of Python programs
- [Bandit](https://bandit.readthedocs.io/en/latest/): Bandit is a tool designed to find common security issues in Python code

We have setup *invoke* commands for ease of command line use. For available commands See

```bash
$ invoke --list=code
Available 'code' tasks:

  .all (.pre-commit)   Runs isort, black pylint, mypy and pytest
  .black               Runs black on all .py files recursively
  .isort               Runs isort on all .py files recursively
  .mypy                Runs mypy on all .py files recursively
  .pylint              Runs pylint on all .py files recursively
  .pytest              Runs pytest
```

The best practice is to run `invoke test.all` and fix all errors before mergin to your MASTER branch and deploying. That will help you develop a Panel site which works and is long term maintainable.

## Remember to Update the Package Requirements

Please note that if you add new features to the the project that depends on one or more not already required Python packages, then those requirements should be added manually to the the relevant file in the `requirements` folder.

## Build and Publish

We use Azure DevOps for build and deployment. You can use find the pipelines [here](https://dev.azure.com/dongenergy-p/TradingAnalytics/_build?definitionScope=%5Cus-trading).

## Docker

The **build process** consist of building 3 images

api_base -> api -> api_test

- api_base contains the basic requirements. It takes a long time to build but does not need to be rebuilt often.
- api contains the api_base image and the package
- api_test is build from the api image, adds and runs the tests and saves test results in the folder /app/test_results. The test results are in the junit format so that they can be published and inspected in Azure Devops.

With a **local installation of Docker** you can replicate the Azure Pipelines build and test pipeline locally.

To build the api image locally run

```bash
invoke docker.build
```

This will be using cached images and layers.

To run the tests inside the api image and export the results to ```./test_results``` run

```bash
invoke docker.test
```

The above commands builds using the cached layers and images, i.e. it is fast. It is not as fast as running the tests locally via the command ```invoke test.all``` though.

Sometimes you need to build from scratch, then you should add the ```--rebuild``` flag.

For more information on available ```Invoke docker.*``` commands use the ```--list``` and ```--help``` flags.

## Deployment

The API is currently not deployed as a seperate python package

## Versioning

We currently don't version this package.

## Contributing

If you are an Ørsted employee or consultant then feel free to contribute.

Please discuss or inform the Lead Platform Architect of important design decissions.

## Authors

- Marc Skov Madsen ([Email](mailto:masma@orsted.dk), [LinkedIn](https://www.linkedin.com/in/marcskovmadsen/))

## License

This project is owned by Ørsted CS Market Trading and can be used and modified by Ørsted employees or consultants only.

[Azure DevOps Build Pipelines](https://dongenergy-p.visualstudio.com/TradingAnalytics/_build)

## Kubernetes

Our config.*.ini files are deployed to k8s as secrets via

```bash
kubectl create secret generic ta-environment-dev --from-file=config.dev.ini
```

and similarly for `test` and `prod` environments.

```bash
kubectl create secret generic ta-environment-prod --from-file=config.prod.ini
```
