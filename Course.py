from db import get_db_connection

def add_course(name, code, instructor_id, department_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Courses (name, code, instructor_id, department_id) VALUES (?, ?, ?, ?)", 
                   (name, code, instructor_id, department_id))
    conn.commit()
    conn.close()

def get_all_courses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    conn.close()
    return courses

def delete_course(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
