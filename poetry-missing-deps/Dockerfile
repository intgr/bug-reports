FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3.10 libpython3.10-dev python3.10-venv python3-pip && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.10 0 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 0 && \
    rm -rf /var/lib/apt/lists/*

# This does not occur when using Python 3.9
#RUN apt-get update && apt-get install -y --no-install-recommends \
#        python3.9 libpython3.9-dev python3.9-venv python3-pip && \
#    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry
# If I don't install these explicitly, Poetry won't work:
# RUN pip install --no-cache-dir cachecontrol crashtest lockfile

RUN poetry -vvv --version

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install -vvv --no-dev --no-root
