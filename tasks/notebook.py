from invoke import task

@task(aliases=("clean", ))
def clean_all(c, ):
    """Strips all notebooks of output.

    Use this to support git diffs and a small repository size"""
    command = (
        "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace src/apps/**/*.ipynb"
    )
    print(command)
    c.run(command)