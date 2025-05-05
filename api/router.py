from fastapi import APIRouter, HTTPException # type: ignore
from .module import Student, Department, Instructor, Course, Enrollment
from db import get_db_connection

router = APIRouter()

# --- STUDENTS ---

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

@router.get("/students/")
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cur.description], row)) for row in rows]

@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students SET first_name=?, last_name=?, email=?, dob=?, gender=?, department_id=?
        WHERE id=?
    """, (student.first_name, student.last_name, student.email, student.dob, student.gender, student.department_id, student_id))
    conn.commit()
    conn.close()
    return {"message": "Student updated successfully"}

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}

# --- DEPARTMENTS ---

@router.post("/departments/")
def create_department(dept: Department):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO departments (name, office) VALUES (?, ?)", (dept.name, dept.office))
    conn.commit()
    conn.close()
    return {"message": "Department added successfully"}

@router.get("/departments/")
def get_departments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM departments")
    rows = cur.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cur.description], row)) for row in rows]

@router.put("/departments/{dept_id}")
def update_department(dept_id: int, dept: Department):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE departments SET name=?, office=? WHERE id=?", (dept.name, dept.office, dept_id))
    conn.commit()
    conn.close()
    return {"message": "Department updated successfully"}

@router.delete("/departments/{dept_id}")
def delete_department(dept_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM departments WHERE id=?", (dept_id,))
    conn.commit()
    conn.close()
    return {"message": "Department deleted successfully"}

# --- INSTRUCTORS ---

@router.post("/instructors/")
def create_instructor(ins: Instructor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO instructors (name, email, department_id) VALUES (?, ?, ?)", (ins.name, ins.email, ins.department_id))
    conn.commit()
    conn.close()
    return {"message": "Instructor added successfully"}

@router.get("/instructors/")
def get_instructors():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM instructors")
    rows = cur.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cur.description], row)) for row in rows]

@router.put("/instructors/{ins_id}")
def update_instructor(ins_id: int, ins: Instructor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE instructors SET name=?, email=?, department_id=? WHERE id=?", (ins.name, ins.email, ins.department_id, ins_id))
    conn.commit()
    conn.close()
    return {"message": "Instructor updated successfully"}

@router.delete("/instructors/{ins_id}")
def delete_instructor(ins_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM instructors WHERE id=?", (ins_id,))
    conn.commit()
    conn.close()
    return {"message": "Instructor deleted successfully"}

# --- COURSES ---

@router.post("/courses/")
def create_course(course: Course):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (title, credits, department_id) VALUES (?, ?, ?)", (course.title, course.credits, course.department_id))
    conn.commit()
    conn.close()
    return {"message": "Course added successfully"}

@router.get("/courses/")
def get_courses():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cur.description], row)) for row in rows]

@router.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE courses SET title=?, credits=?, department_id=? WHERE id=?", (course.title, course.credits, course.department_id, course_id))
    conn.commit()
    conn.close()
    return {"message": "Course updated successfully"}

@router.delete("/courses/{course_id}")
def delete_course(course_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    conn.close()
    return {"message": "Course deleted successfully"}

# --- ENROLLMENTS ---

@router.post("/enrollments/")
def create_enrollment(enroll: Enrollment):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO enrollments (student_id, course_id, instructor_id) VALUES (?, ?, ?)", (enroll.student_id, enroll.course_id, enroll.instructor_id))
    conn.commit()
    conn.close()
    return {"message": "Enrollment added successfully"}

@router.get("/enrollments/")
def get_enrollments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM enrollments")
    rows = cur.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cur.description], row)) for row in rows]

@router.delete("/enrollments/{enroll_id}")
def delete_enrollment(enroll_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM enrollments WHERE id=?", (enroll_id,))
    conn.commit()
    conn.close()
    return {"message": "Enrollment deleted successfully"}
