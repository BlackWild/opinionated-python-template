# Python docker image variant passed to DockerFile via the `devcontainer.json` file
ARG PYTHON_VARIANT

# Base image
FROM python:${PYTHON_VARIANT}

# Other arguments
ARG PIPX_VERSION
ARG POETRY_VERSION

# Install `pipx` and ensure its directory is in the PATH
RUN python3 -m pip install --user pipx==${PIPX_VERSION}
RUN python3 -m pipx ensurepath
# `pip install --user` installs in ~/.local/bin
# keep that in mind when using `pipx` in this DockerFile

# Install `poetry` with `pipx`
RUN ~/.local/bin/pipx install poetry==${POETRY_VERSION}