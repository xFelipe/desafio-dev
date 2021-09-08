FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /code
COPY Pipfile /code/

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN apt-get autoremove -y gcc
# RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]