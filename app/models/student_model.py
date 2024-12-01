from pydantic import BaseModel, Field
from typing import Dict, Optional

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address
    
class StudentUpdateRequest(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(BaseModel):
    id: str
