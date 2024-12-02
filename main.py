import os
from fastapi import FastAPI
from app.routes.student_routes import router as student_router
from dotenv import load_dotenv

# Load environment variables from a .env file (optional, useful for local development)
load_dotenv()

# Access the MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in the environment variables.")

# Initialize FastAPI app
app = FastAPI(title="Student Management System")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Include student-related routes
app.include_router(student_router, prefix="/api/v1/students")
