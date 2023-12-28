# About this project

This repository contains an opinionated template structure for modern Python projects. The goal is to use latest frameworks and technologies introduced in the Python ecosystem without compromising stability.

The aim is not to overwhelm you with millions of tools which makes the decision-making difficult. I also try to explain the decisions behind choosing a tool to give some context to the decisions.

## Intended audience

This project is intended for intermediate developers who have acquired the basic knowledge of Python and programming in general but are struggling finding a good starting point for their Python projects in terms of code quality.

With that being said, I try to write everything in simple and understandable terms so that it is useful for beginners or professionals alike.

## Main ideas

There are a few basic principles that we follow to design the structure of the codebase. If you find them appealing, it means you will enjoy and appreciate using this template. We believe the standard Python, despite being a very popular programming language, surprisingly lacks the developer experience (DX) it deserves. The goal of this template is to provide this DX.

Things we would like to achieve:

- Everything about the project should be confined in the project code base. There should be no dependency on or confusion with packages that are locally installed on your system. This ensures consistency of the development environment.

- Next, we must have specific style and code quality rules that are checked at every level of development. For this purpose, we config every formatter and linter we use in their local config files and have our IDE extensions and `pre-commit` hooks to check the code based on them. This ensures reproducibility of the development environment and guards the project code quality rules.

- We encourage static typing and type annotation for functions and variables. Python as a dynamically typed language does not completely follow this practice but has enough tools we can use to force this practice. We use a combination of linting rules and static type checkers to achieve that.

- We also include other important parts like unit testing, documentation, and so on to provide a rich set of tools for your project.

# How to use this template?

Here, you will find a short version of how to use this project template. However, you are strongly recommended to read through [The Structure](#the-structure) section down below to fully understand the decisions behind the tools used.

You need to have these software installed on your computer:

- Visual Studio Code [link](https://code.visualstudio.com)
  - `Dev Containers` extension [link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Docker Desktop [link](https://www.docker.com/products/docker-desktop/)
- Git

Nothing more is required, not even Python. Everything will be handled for you by the above tools. Docker prepares the development environment and vscode interacts with it.

To start using the template, you need to download the code repository as a zip file, extract it in any folder you want, initialize a git repository in it, and start developing your project. It has everything included but you need to change a few things before starting

Required changes:

- In the template, the name of the project is set to `opinionated_python`, feel free to change this and the corresponding folder in the `src/` folder to whatever you like
- Change the project details such as name, description, author and so on in the `pyproject.toml` file.

Optional changes:

- Check the versions of `python`, `pipx`, and `poetry` in the `.devcontainer/devcontainer.json` and see if your project needs to change them. I suggest not changing them unless you absolutely need to.

> If you change the `python` version, you would also need to change the python package dependency in the `pyproject.toml` file accordingly.

> Also as a general rule, feel free to change the versions of the default tools (linter, formatter, ...) in the `pyproject.toml` file if you would like to. It is not guarantied that the versions in the template are the latest. If you decide to change the versions, I suggest you use somewhat fixed versions in order to avoid breaking changes in future updates of the packages. You might also want to change the corresponding versions in the `pre-commit` config file at `.pre-commit-config.yaml` accordingly.

Finally:

- Now, you are ready to go. You just need to open the folder in vscode. Having the `Dev Containers` extension installed, it will automatically prompt you to open the project in the dev container. Click yes, and wait for the container to start (make sure Docker is running beforehand).
- After the container starts, you have your python dev environment ready. You can run
  ```bash
  poetry install
  ```
  to install the dependencies (do this in the beginning to install the DX tools). You can run
  ```bash
  poetry add ***
  ```
  to add any package to your project dependencies. For more commands, you can read `poetry` documentation at [here](https://python-poetry.org/docs/)
- Have fun developing your project!

# The structure

Let us go through the structure of this template. The logic of building the structure goes more or less in the same order as introduced in the following.

## Development environment

The main point here is to contain everything about the project inside the codebase and make it reproducible. Everything should run on any computer the same. We use the following for this purpose.

### Version control

We start with `git` and initialize a git repository. There is not much more to say here. This is how we achieve eternal history for the project.

### IDE

We use Visual Studio Code.

### Development container

We would like to isolate everything to the project itself. This means we don't want to even install Python itself on the computer. For that, we use development containers. We need `Docker` and `Development Containers` to do the job.

This is defined in the `.devcontainer` folder. It consists of a basic `devcontainer.json` file also including the suggested vscode extensions for the environment and a `Dockerfile`.

We use somewhat fixed versions for the things we install in order to avoid breaking changes in Python updates. The versions are set in the `devcontainer.json` filed and used when building the Docker development container image.

The Docker image is just a base `python` image with `pipx` and `poetry` installed in it.

## Package structure

Next, we need to design a structure for the Python package.

### On avoiding `pip`

We don't use `pip` directly. The reason is that we believe it is not a very stable tool to rely on for proper packaging. We want absolute control over the dependency packages we install and the location of the installation. Modern development practice suggests installing dependency packages locally in the project folder and not system-wide.

### Package manager

We use `poetry` as our package manager. It handles installing dependencies, building the project, and publishing. `poetry` is installed as part of the development container.

To have better control over project configuration, we separate the Python project configuration and `poetry`-specific configs in different files. For the project, we use the standard `pyproject.toml` file and keep `poetry` configs in the `poetry.toml` file.

It is important to force `poetry` to install all the packages locally in the project folder. We use the `in-project = true` flag in the `poetry.toml` config which will make `poetry` create a local `.venv` folder. Every dependency package is then installed there and it works similar to the `node_modules` folder in JavaScript.

## Code quality

We use a few tools to keep the code high-quality. Each tool will have its own config file in the project and their corresponding vscode extension will be automatically installed during the Development Container startup.

It is also important to note that the code quality checks are done at several levels. First, locally by the vscode extensions. Second, before committing changed files to git using `pre-commit`, and lastly by GitHub Actions on the whole project (not implemented yet). This helps guarding the code quality rules defined for the project and ensures that you have less headache looking for inconsistencies in code as the project grows large.

### Linting

We use `ruff`. It is fast and reliable. Configuration file is at `ruff.toml`. In the current implementation of the template, all linting rules are selected and a few unused ones are explicitly excluded. I suggest you also follow the same practice and try to exclude rules you don't like while developing your project. You must have compelling reasons for excluding a rule.

### Static typing

For static typing, we use `pyright`.

Some of the rules like function input and return annotation are also checked through `ruff`, but `pyright` also checks if the annotations are actually correct by analyzing the types. We use the strict mode.

The configurations for static typing is located at the `pyrightconfig.json` file.

> The decision of choosing `pyright` is partly because we wanted to use vscode's Pylance language server and it is based on `pyright`. In order to keep everything consistent, we set pre-commit hooks with `pyright` and use the Pylance extension while coding in the IDE. This is how we make `pyright` and Pylance work together (otherwise, the two pyright and Pylance extensions of vscode do not work together).

### Style

For styling, we use `black`. It is already highly opinionated and there is no configuration file corresponding to it in this template.

## Documentation

Here, you will find the tools used for proper documentation in this template.

### Code documentation

For code documentation we use `docstring`s (`google` style convention). This means that we require all files, classes, and functions to have `docstring`s as well as type annotations so that the project documentation website can be generated based on them.

Do not include type definitions in the `docstring`s and have type definitions only in the python code files. The project documentation tool will recognize them and generate api documentations correctly.

The `docstring` standards are checked by our linter `ruff` so you can use the warnings and hints to keep the code and the `docstring`s neat.

### Project documentation

The documentation of the project is created using `mkdocs`.

The project documentation has two parts:

- Static: a series of Markdown files in the `docs/` directory of the project which includes tutorials and guides and the whole structure of the documentation site
- Dynamic: which is generated automatically using the `mkdocstrings-python` package when `mkdocs` is generating the documentation website. `mkdocstrings` scans the source codes of the project and generates api references using the type annotations and docstrings of functions and classes defined in the code. This means that you should to write proper docstrings for everything.

We use the `mkdocs-material` theme for the documentation website. The package is actually much more than just a theme and has a lot of built-in features that we can use.

##### How to use `mkdocs`

To start the watcher and generate the documentation website temporarily, you should use

```bash
mkdocs serve
```

This command will build the site and watch for changes, and will serve it on localhost. The exact IP and port will be printed in console after running this command.

Also to generate the whole site you can use the command

```bash
mkdocs build
```

This will generate the complete deployable website in the local folder. Do not commit the generated site to git.

## Repository management

### Pre-commit hooks

In order to prevent unchecked code to be committed to the repo, we use `pre-commit` hooks. The hooks are designed to work with local configuration files of the code quality tools.

IMPORTANT:
In any copy of this template on your local development machine, you must run

```bash
pre-commit install
```

so that the hooks are installed in git.

### CI/CD

To be added...

## Unit testing

Here, you will find the tools used in this template for unit testing and coverage.

### Unit testing framework

For unit testing, we use `pytest`.

All the test files are stored in the `tests/` directory. Keep in mind that `pytest` will automatically look for tests in that directory but you should pay attention to these points:

- For `pytest` to collect the test, you should prefix the name of the test files with `test_*.py`
- The name of very function to test should start with `test_*` and every class name should start with `Test_*`

You can use the command

```bash
pytest
```

to check out the test results.

### Code coverage

For code coverage, we use `pytest-cov`, an extension for `pytest`. It is based on another popular package `coverage` and it actually installs the binaries of `coverage` so you can also use that in your terminal.

Anyways, in order to generate coverage reports you should run

```bash
pytest --cov
```

This will print the report in terminal and generate a `.coverage` report file.

## Miscellaneous tools

Here, you will find other tools included in this template.

### Editor configuration

We use `EditorConfig` to ensure consistency of handling files and general stylistic guidelines across IDEs. It is configured via the `.editorconfig` file.

### Other styling

Style and file formatters act in this order:

- Python files are formatted using `black`
- `.toml` configure files are formatted using the vscode extension
- All other files in the project are formatted using `prettier`

### Spellchecking

For spell checking, we use Street Side Software's `cspell`. It has a vscode extension as well as a `pre-commit` hook which we have set up. It uses the local `cspell.json` config file.

This means it is a good idea to add any unrecognized spelling specific to your project to the `cspell.json`'s word list so that it is shared with everyone working on the project.

# Contribution

Feel free to open an issue in the project repo [here](https://github.com/BlackWild/opinionated-python-template/issues).
