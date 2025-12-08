# Vollwertige Basis für Python/AI-Entwicklung
FROM python:3.12

# 1. System-Tools installieren (inkl. git)
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    vim \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. uv installieren (offizieller Installer)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. PATH erweitern, damit uv verfügbar ist
ENV PATH="/root/.local/bin:/root/.cargo/bin:${PATH}"

# 4. Standard-Arbeitsverzeichnis im Container
WORKDIR /workspaces/app

CMD ["bash"]
