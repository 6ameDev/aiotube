# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the FastAPI server
COPY server/ server/

# Install dependencies
RUN pip install --no-cache-dir -r server/requirements.txt

# Install your forked version of aiotube from GitHub
RUN pip install --no-cache-dir git+https://github.com/6ameDev/aiotube.git@videos-metadata

# Expose the FastAPI server port
EXPOSE 8000

# Command to run FastAPI server
CMD ["uvicorn", "server.server:app", "--host", "0.0.0.0", "--port", "8000"]
