# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (modify if needed)
EXPOSE 5000

# Run the app
CMD ["python", "demo.py"]