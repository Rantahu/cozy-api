FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Setup Debian linux
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install build-essential curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

WORKDIR /app
COPY . /app

RUN pip install -r /requirements/local.txt

COPY ./bin/start.sh /start.sh
COPY ./bin/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chmod +x /start.sh

ENTRYPOINT ["/entrypoint.sh"]
