from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    dob: Optional[str] = None
    gender: Optional[str] = None
    department_id: Optional[int] = None

class Department(BaseModel):
    name: str
    office: Optional[str] = None

class Instructor(BaseModel):
    name: str
    email: str
    department_id: Optional[int] = None

class Course(BaseModel):
    title: str
    credits: int
    department_id: int

class Enrollment(BaseModel):
    student_id: int
    course_id: int
    instructor_id: int
