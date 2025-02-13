# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the working directory in the container
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Run the FastAPI app with Uvicorn (Make sure you have uvicorn installed)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
