FROM python:3.7-buster

# Install Buildozer dependencies, including OpenJDK 11
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
    openjdk-11-jdk \
    libffi-dev \
    libpython3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Cython and Buildozer
RUN pip install --upgrade pip && \
    pip install cython==0.29.36 buildozer

WORKDIR /app
CMD ["buildozer", "android", "debug"]
