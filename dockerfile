# Use a slim Python base image for efficiency
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Flask (add other dependencies as needed)
RUN pip install flask

# Expose port 5000 to allow external access to the app
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP=main.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
