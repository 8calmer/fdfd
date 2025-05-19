FROM python:3.7-buster

# Install AdoptOpenJDK 8
RUN apt-get update && apt-get install -y wget apt-transport-https gnupg && \
    wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add - && \
    echo "deb https://adoptopenjdk.jfrog.io/adoptopenjdk/deb buster main" | tee /etc/apt/sources.list.d/adoptopenjdk.list && \
    apt-get update && apt-get install -y adoptopenjdk-8-hotspot && \
    rm -rf /var/lib/apt/lists/*

# Install Buildozer dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libsqlite3-dev \
    python3-dev \
    python3-pip \
    libffi-dev \
    libpython3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Cython and Buildozer
RUN pip install --upgrade pip && \
    pip install cython==0.29.36 buildozer

WORKDIR /app
CMD ["buildozer", "android", "debug"]
