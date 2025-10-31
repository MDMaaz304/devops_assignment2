# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app folder contents
COPY app/ .

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
