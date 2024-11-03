# Dockerfile
FROM python:3.8-slim

WORKDIR /app

# Install Flask and MySQL connector
RUN pip install flask mysql-connector-python

# Copy the app code and templates folder
COPY app.py .
COPY templates/ templates/

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose port 5000 for the app
EXPOSE 5000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
