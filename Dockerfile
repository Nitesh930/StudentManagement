FROM python:3.9-slim

WORKDIR /app

# Copy the entire project into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

# Start FastAPI with Gunicorn and Uvicorn worker
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:10000"]
