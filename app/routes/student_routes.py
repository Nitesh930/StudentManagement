from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional

from pydantic import BaseModel
from app.models.student_model import StudentCreate, StudentUpdateRequest, StudentResponse
from app.database.database import student_collection
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    student_dict = student.model_dump()
    result = await student_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@router.get("/", response_model=dict)
async def get_students(country: Optional[str] = Query(None), age: Optional[int] = Query(None)):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}

    students_cursor = student_collection.find(filters)
    students = await students_cursor.to_list(length=100)
    return {"data": [{"name": s["name"], "age": s["age"]} for s in students]}

@router.get("/{id}", response_model=dict)
async def get_student_by_id(id: str):
    if not id:
        raise HTTPException(status_code=400, detail="Student ID is required.")
    
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format.")

    student = await student_collection.find_one({"_id": ObjectId(id)})
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    
    return {
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }

class StudentUpdateRequest(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[dict] = None
@router.patch("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(id: str, student: StudentUpdateRequest):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format.")
    update_data = {k: v for k, v in student.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update.")
    result = await student_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format.")
    result = await student_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return
