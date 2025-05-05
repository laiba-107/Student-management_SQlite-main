from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    dob: str
    gender: str
    department_id: int

class Department(BaseModel):
    name: str
    office: str

class Instructor(BaseModel):
    name: str
    email: str
    department_id: int

class Course(BaseModel):
    title: str
    credits: int
    department_id: int

class Enrollment(BaseModel):
    student_id: int
    course_id: int
    instructor_id: int
