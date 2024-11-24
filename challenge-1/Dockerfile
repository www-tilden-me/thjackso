# Use a lightweight Python image
FROM python:3.9-slim

# Flag provided by cmgr. This is just a default
ARG FLAG="picoctf{default_flag}"

# Set the working directory
WORKDIR /app


# Copy necessary files to the container
COPY challenge.py .
COPY setup.py .

# Install required dependencies
RUN pip install pycryptodome

# Run setup.py to generate or prepare any files needed
RUN python3 setup.py

# Create metadata for cmgr
RUN mkdir /challenge && chmod 700 /challenge
RUN echo "{\"flag\": \"$(cat flag)\"}" > /challenge/metadata.json
RUN tar zcf /challenge/artifacts.tar.gz challenge.py

# Expose the port the server will listen on
EXPOSE 8888
# PUBLISH 8888 AS port

# Run the challenge script
CMD ["python3", "challenge.py", "--host", "0.0.0.0", "--port", "8888"]
