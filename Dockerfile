# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from your D:\project directory into the container
COPY . /app

# Ensure the output directory exists
RUN mkdir -p /app/output

# Set the command to run the Python script
CMD ["python", "/app/script.py"]
