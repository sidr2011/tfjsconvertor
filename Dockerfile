# syntax = docker/dockerfile:1.4

# Use the conda/s2i-anaconda-project-ubi8 as the base image
FROM  ultralytics/ultralytics:latest AS builder

# Copy the project files into the Docker image
COPY app /app
WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Sleep for 3 hours
CMD ["sleep", "10800"]

# Command to run the application
# CMD ["python", "recycle.py"]

