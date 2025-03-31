# Recommendations demo

A scratch repo for playing out some initial implementations of a recommendation algorithm

This is a [`uv` project](https://docs.astral.sh/uv/guides/projects/).

## Quickstart


## Notebook quickstart

https://docs.astral.sh/uv/guides/integration/jupyter/#using-jupyter-from-vs-code

We're still working on our development environment so for now, we're using the `.venv` for our python kernal



## Package management & maintenance

To install pre-commit hooks:
```
uv run pre-commit install
```

To add a new dependency:
```
uv add <package name>
```

To remove a dependency:
```
uv remove <package name>
```

## Managing uv and Docker

Our docker setup is directly pulled from Astral's GitHub repo demonstrating `uv`/`docker` best practices for local development

This is a faily naive implementation so we recommend starting from `uv`'s [docker integration documentation](https://docs.astral.sh/uv/guides/integration/docker/#getting-started) as well as their [Github repo](https://github.com/astral-sh/uv-docker-example) demonstrating `uv`/`docker` best practices.
