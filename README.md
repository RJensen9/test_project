# test_project

Test project to see if this works

## Quick start:
If cloning this repo, run these commands to set up the environment for development:
```shell
git clone <this-repo.git>
cd  <this-repo-url>

# We recommend using `pyenv` to manage multiple python versions. If pyenv is installed, just run:
pyenv install 3.9.13 # or whatever >=3.9 version you'd prefer
pyenv local 3.9.13

# ...OR if you don't use pyenv, run:
poetry env use c:\path\to\python3.9\python.exe # Windows
poetry env use /path/to/python39 # Linux/Mac

# install libraries
poetry install

# install pre-commit hooks for code quality etc
pre-commit install

# run tests locally
pytest

```
Other useful commands include:
```shell

# generate html doc
scripts\gen-doc # Windows
scripts/gen-doc # Linux/Mac

# Add private pypi index for adding and publishing packages
poetry source add --secondary csiroenergy https://pkgs.dev.azure.com/csiro-energy/csiro-energy/_packaging/csiro-python-packages/pypi/simple/
poetry config repositories.csiroenergy https://pkgs.dev.azure.com/csiro-energy/csiro-energy/_packaging/csiro-python-packages/pypi/upload
poetry config http-basic.csiroenergy YOUR_IDENT YOUR_TOKEN # Generate a token at https://dev.azure.com/csiro-energy/_usersSettings/tokens

# build a redistributable python package
poetry build

# publish a built wheel to the private csiroenergy pypi repo. Only works once for each unique project version (in pyproject.toml).
poetry publish -r csiroenergy

# build a docker image, and define two containers, one for tests, and one for launching your code
docker-compose build

# run tests in docker container
docker-compose run test
```

## Installation Instructions

For detailed installation instructions see the template readme [here](docs/README.md)
