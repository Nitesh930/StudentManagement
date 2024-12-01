#!/bin/bash

# Activate any virtual environment if needed
# . venv/bin/activate

# Run the FastAPI app using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8080
