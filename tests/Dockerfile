FROM mcr.microsoft.com/playwright/python:v1.55.0-noble

ENV TZ=Europe/London \
    LANG=en_GB.UTF-8 \
    LC_ALL=en_GB.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      python3 \
      fonts-liberation \
      fonts-dejavu-core \
      fonts-dejavu-extra \
      nodejs \
      npm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /design-system


COPY package.json .
COPY package-lock.json .
COPY dev-requirements.txt .
RUN rm -rf node_modules

RUN pip install --no-cache-dir -r dev-requirements.txt
RUN pip install setuptools

RUN npm ci --include=dev

COPY tests/ ./tests/
COPY src-site/ ./src-site/
COPY system/ ./system/
COPY .eleventy.js .


#CMD bash
CMD pytest -sx
