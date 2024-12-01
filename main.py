from fastapi import FastAPI
from app.routes.student_routes import router as student_router

app = FastAPI(title="Student Management System")

# Include student-related routes
app.include_router(student_router, prefix="/api/v1/students")
