FROM mcr.microsoft.com/playwright/python:v1.46.0-jammy
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip && \
    pip install -e .[dev] && \
    python -m playwright install --with-deps
CMD ["pytest", "-q"]
