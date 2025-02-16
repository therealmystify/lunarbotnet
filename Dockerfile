# Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port (if your app listens on a port)
EXPOSE 5000

# Run the Python app
CMD ["python", "app.py"]
