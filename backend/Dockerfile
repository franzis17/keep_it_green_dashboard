# Use Python 3.10 slim image (fewer pre-installed packages)
FROM python:3.10-slim

# Set working directory in container, next commands will be executed within this directory
WORKDIR /app

# Install system dependencies needed for PostgreSQL + remove cached package lists
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements from local machine to container (after doing `pip freeze > requirements.txt`)
COPY requirements.txt .
# Install python dependencies, do not store temp files to keep docker image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files from project directory to /app directory inside container
COPY . .

# Create a user AND recursively change ownership of each files in /app
RUN useradd -m franz && chown -R franz:franz /app
# Switch to user, next commands will be executed as this user
USER franz

# Expose port 8000, tells docker to listen on port 8000
EXPOSE 8000

# Run the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
