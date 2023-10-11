DockerfileCopy code# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port that Flask is running on
EXPOSE 5000

# Run the flask application
CMD ["flask", "run", "--host=0.0.0.0"]