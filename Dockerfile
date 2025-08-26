# Use an official Python image
FROM python:3.12.3
# Set working directory in the container
WORKDIR /home/app

# Copy dependency list first (better for caching layers)
COPY requirements.txt .

# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the application
CMD ["docker", "pull", "qdrant/qdrant"]
CMD ["streamlit", "run", "frontend/app.py"]
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
