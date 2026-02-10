FROM python:3.12-slim

# Install opengrep via install script
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh | bash \
    && apt-get purge -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Symlink opengrep onto PATH
RUN ln -s "$(find /root/.opengrep -name opengrep -type f | head -1)" /usr/local/bin/opengrep

# Install Python dependencies
COPY requirements.txt /runtime/requirements.txt
RUN pip install --no-cache-dir -r /runtime/requirements.txt

# Copy runtime code
COPY test-runner.py /runtime/test-runner.py
COPY checks.py /runtime/checks.py

WORKDIR /rules
ENTRYPOINT ["python", "/runtime/test-runner.py"]
