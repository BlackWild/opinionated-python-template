# What is this?

This repository contains an opinionated structure for modern Python projects. The goal is to use latest frameworks and technologies introduced in the Python ecosystem without compromising stability.

## Intended audience

This project is intended for intermediate developers who have acquired the basic knowledge of Python and programming in general but are struggling finding a good starting point for their Python projects in terms of code quality.

With that being said, I try to write everything in simple and understandable terms so that it is useful for beginners or professionals alike.

## Main ideas

There are a few basic principles that we follow to design the structure of the codebase. If you find them appealing, it means you will enjoy and appreciate using this repo.

- Standard Python, despite being a very popular programming language, surprisingly lacks the developer experience (DX) it deserves.

# How to use this?

Here, you will find a short version of how to use this project template. However, you are strongly suggested to read through The Structure [link??] section to fully understand the decisions behind the tools used.

You need to have these software installed on your computer:

- Visual Studio Code [link]
  - `Dev Containers` extension [link]
- Docker [link]
- Git [link]

Nothing more is required, not even Python. Everything will be handled for you by the above tools. Docker prepares the development environment and vscode interacts with it.

To start using the template, you need to download the project via the release section here [????]. It has everything included but you need to change a few things before starting

Required changes:

- Change the project details such as name, description, author and so on in the `pyproject.toml` file.

Optional changes:

- Check the versions of `python`, `pipx`, and `poetry` in the `.devcontainer/devcontainer.json` and see if your project needs to change them. I suggest not changing them unless you absolutely need to.

> If you change the `python` version, you would also need to change the python package dependency in the `pyproject.toml` file accordingly.

# The structure

Let us go through the structure that is implemented in this repo. The logic of building the structure goes more or less in the same order as introduced int he following.

## Development environment

The main point here is to contain everything about the project inside the codebase and have it reproducible. Everything should run on any computer the same. We use the following for this purpose.

### Version control

We start with `git` and initialize a git repository. There is not much more to say here. This is how we achieve eternal history for the project.

### IDE

We use Visual Studio Code.

### Development container

We would like to isolate everything to the project itself. This means we don't want to even install Python itself on the computer. For that, we use development containers. We need `Docker` and `Development Containers` to do the job.

This is defined in the `.devcontainer` folder. It consists of a basic `devcontainer.json` file also including the suggested vscode extensions for the environment and a `Dockerfile`.

We use somewhat fixed versions for the things we install in order to avoid breaking changes in Python updates. The versions are set in the `devcontainer.json` filed and used when building the Docker development container image.

## Package structure

Next, we need to design a structure for the Python package.

### On avoiding `pip`

We don't use `pip` directly. The reason is that we believe it is not a very stable tool to rely on for proper packaging. We want absolute control over the dependency packages we install and the location of installation. Modern development practice suggests installing dependency packages locally in the project folder and not system-wide.

### Package manager

We use `poetry` as our package manager. It handles installing dependencies, building the project, and publishing. `poetry` is installed as part of the development container.

To have better control over project configuration, we separate the Python project configuration and `poetry`-specific configs in different files. For the project, we use the standard `pyproject.toml` file and keep `poetry` configs in the `poetry.toml` file.

It is important to force `poetry` to install all the packages locally in the project folder. We use the `in-project = true` flag in the `poetry.toml` config which will make `poetry` creating a local `.venv` folder. Every dependency package is then installed there and it works similar to the `node_modules` folder in JavaScript.

## Code quality

We use a few tools to keep the code high quality. Each tool will have its own config file in the project and their corresponding vscode extension will be automatically installed during the Development Container startup.

It is also important to note that the code quality checks are done at several levels. First, locally by the vscode extensions. Second, before committing changed files to git using `pre-commit`, and lastly by GitHub Actions on the whole project [???]. This helps guarding the code quality rules defined for the project and ensures that you have less headache looking for inconsistencies in code as the project grows large.

### Linting

We use `ruff`. It is fast and reliable.

### Static typing

### Style

## Documentation

### Code documentation

### Project documentation

## Repository management

### Pre-commit hooks

### CI/CD

## Unit testing

### Test framework

### Code coverage

## Miscellaneous tools

### Editor configuration

### Other styling

### Spellchecking
