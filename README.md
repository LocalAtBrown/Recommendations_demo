# Recommendations demo

A scratch repo for playing out some initial implementations of a recommendation algorithm

This is a [`uv` project](https://docs.astral.sh/uv/guides/projects/). Development, both local terminal and docker
are passed through `uv`.

## Initialization

This project is managed as .

To run the application outside of docker:
```zsh
uv run rec-demo
```

To run various


## Maintainence

Project maintainence is passed through `uv`

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
