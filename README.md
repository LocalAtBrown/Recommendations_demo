# Recommendations demo

A scratch repo for playing out some initial implementations of a recommendation algorithm


## Initialization

This project is managed as a [`uv` project](https://docs.astral.sh/uv/guides/projects/).

To run the application outside of docker:
```zsh
uv run rec-demo
```

To run various


## Maintainence

Project maintainence is passed through `uv`

```
uv run pre-commit install
```

`rec-demo` dependencies are managed within the `pyproject.toml` file.

To add a new dependency:
```
uv add <package name>
```

To remove a dependency:
```
uv remove <package name>
```
