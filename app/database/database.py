from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb+srv://singhniteshkumar1234:8h2O8PT9x3CveR8f@cluster0.irk35.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.student_db  
student_collection = database.get_collection("students")
