FROM mcr.microsoft.com/playwright/python:v1.55.0-noble

ARG USER_ID=1000
ARG GROUP_ID=1000

ENV TZ=Europe/London \
    LANG=en_GB.UTF-8 \
    LC_ALL=en_GB.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    fonts-liberation \
    fonts-dejavu-core \
    fonts-dejavu-extra \
    curl

# Install Node.js 18 and npm 10
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@10 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create user with matching host UID/GID or use existing one
RUN if ! getent group ${GROUP_ID} > /dev/null 2>&1; then \
    groupadd -g ${GROUP_ID} testuser; \
    fi && \
    if ! getent passwd ${USER_ID} > /dev/null 2>&1; then \
    useradd -u ${USER_ID} -g ${GROUP_ID} -m -s /bin/bash testuser; \
    fi

WORKDIR /design-system

# Python stuff
COPY dev-requirements.txt .
RUN pip install --no-cache-dir -r dev-requirements.txt
RUN pip install setuptools


# NPM Stuff
COPY package.json .
COPY package-lock.json .
RUN rm -rf node_modules
RUN npm ci --include=dev

# Copy code over
COPY .eleventy.js .
COPY tests/ ./tests/
COPY tests/ ./tests/
COPY system/ ./system/
COPY src-site/ ./src-site/

# Change ownership of the working directory to the user with matching UID
RUN find /design-system \
    \( -type d -name node_modules -o -path '*/tests/screenshots/baseline' \) -prune \
    -o -exec chown -h ${USER_ID}:${GROUP_ID} {} +

USER ${USER_ID}

CMD ["pytest", "-sx", "-p", "no:cacheprovider"]
