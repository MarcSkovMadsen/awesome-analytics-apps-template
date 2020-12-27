"""Invoke tasks for working with notebooks"""
from invoke import task


@task(aliases=("clean",))
def clean_all(
    context,
):
    """Strips all notebooks of output.

    Use this to support git diffs and a small repository size"""
    command = (
        "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace src/apps/**/*.ipynb"
    )
    print(command)
    context.run(command)
