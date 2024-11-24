# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy necessary files to the container
COPY challenge.py .
COPY setup.py .

# Install required dependencies
RUN pip install pycryptodome

# Run setup.py to generate or prepare any files needed
RUN python3 setup.py

# Expose the port the server will listen on
EXPOSE 8888

# Run the challenge script
CMD ["python3", "challenge.py", "--host", "0.0.0.0", "--port", "8888"]
