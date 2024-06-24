# Use the official Python image from the Docker Hub
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
