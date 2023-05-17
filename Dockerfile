# Use the official Python base image
FROM python:3.10.5

# Set the working directory
WORKDIR /api

# Install packages
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /api

# Expose the port the app will run on
EXPOSE 6000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0 
ENV FLASK_RUN_PORT=6000



# Start the Flask application
CMD flask run --host=0.0.0.0 --port=6000
