from fastapi import APIRouter
from .module import Student, Department, Instructor, Course, Enrollment
from db import get_db_connection

router = APIRouter()

# Students
@router.post("/students/")
def create_student(student: Student):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, dob, gender, department_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student.first_name, student.last_name, student.email, student.dob, student.gender, student.department_id))
    conn.commit()
    conn.close()
    return {"message": "Student added successfully"}

# Departments
@router.post("/departments/")
def create_department(dept: Department):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO departments (name, office)
        VALUES (?, ?)
    """, (dept.name, dept.office))
    conn.commit()
    conn.close()
    return {"message": "Department added successfully"}

# Instructors
@router.post("/instructors/")
def create_instructor(ins: Instructor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO instructors (name, email, department_id)
        VALUES (?, ?, ?)
    """, (ins.name, ins.email, ins.department_id))
    conn.commit()
    conn.close()
    return {"message": "Instructor added successfully"}

# Courses
@router.post("/courses/")
def create_course(course: Course):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO courses (title, credits, department_id)
        VALUES (?, ?, ?)
    """, (course.title, course.credits, course.department_id))
    conn.commit()
    conn.close()
    return {"message": "Course added successfully"}

# Enrollments
@router.post("/enrollments/")
def create_enrollment(enroll: Enrollment):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO enrollments (student_id, course_id, instructor_id)
        VALUES (?, ?, ?)
    """, (enroll.student_id, enroll.course_id, enroll.instructor_id))
    conn.commit()
    conn.close()
    return {"message": "Enrollment added successfully"}
