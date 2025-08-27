# Use an official Python image
FROM python:3.12.3
# Set working directory in the container
WORKDIR /home

# Copy dependency list first (better for caching layers)
COPY requirements.txt .

# Install dependencies if requirements.txt exists
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY frontend/ ./frontend

# Command to run the application
CMD ["streamlit", "run", "frontend/app.py"]
