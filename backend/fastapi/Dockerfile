FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY ./src /app/src
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

# Run the server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
