# Use the official Python image from the Docker Hub
FROM python:3.11-slim-buster


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Debug: Show the contents of requirements.txt
RUN cat /app/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for the application
EXPOSE 8000

# Run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
