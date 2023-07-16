FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    gettext \
    git \
    libpq-dev \
    postgresql-client \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
COPY nginx/nginx.default /etc/nginx/sites-available/default
RUN useradd -ms /bin/bash app
USER app
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV  PATH="/home/app/.local/bin:$PATH"
WORKDIR /home/app/
COPY pyproject.toml poetry.lock ./
RUN /home/app/.local/bin/poetry export -f requirements.txt --output requirements.txt
USER root
RUN pip install -r requirements.txt
COPY . .
COPY entrypoint/start-server.sh /home/app/
RUN chmod +x /home/app/start-server.sh && chown -R app:app /home/app
EXPOSE 8010
ENTRYPOINT [ "/bin/bash", "/home/app/start-server.sh" ]