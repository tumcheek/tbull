FROM python:3.12.3-alpine

# Set the working directory
WORKDIR /usr/src/tbull

# Set environment variables to ensure a clean, reproducible environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies required for psycopg2 (PostgreSQL adapter)
RUN apk update && apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# Upgrade pip and install project dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/tbull/entrypoint.sh
RUN chmod +x /usr/src/tbull/entrypoint.sh

# Copy project
COPY . .

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/tbull/entrypoint.sh"]