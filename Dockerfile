# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables (optional, but good practice)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents (including app.py) into the container at /app
COPY . /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Run the Flask app when the container starts
CMD ["python", "app.py"]
