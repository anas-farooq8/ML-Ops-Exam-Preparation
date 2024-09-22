# Use an official Python runtime as a base image
FROM python:3.10.0a7-slim-buster

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the outside world
EXPOSE 5000

# Run the Flask app
CMD ["python", "test.py"]

# docker build -t add-app .