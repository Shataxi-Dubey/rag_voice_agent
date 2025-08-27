# Use an official Python image
FROM python:3.12.3
# Set working directory in the container
WORKDIR /home

# Copy dependency list first (better for caching layers)
COPY requirements.txt .
COPY .env .

# Install dependencies if requirements.txt exists
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY backend/ ./backend

# Command to run the application
CMD ["uvicorn", "backend.main:rag_voice_agent_api", "--host", "0.0.0.0", "--port", "8000"]
