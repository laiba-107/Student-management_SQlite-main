from db import get_db_connection

def enroll_student(student_id, course_id, grade=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (?, ?, ?)", 
                   (student_id, course_id, grade))
    conn.commit()
    conn.close()

def get_all_enrollments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.id, s.name, c.name, e.grade 
        FROM Enrollments e
        JOIN Students s ON e.student_id = s.id
        JOIN Courses c ON e.course_id = c.id
    """)
    enrollments = cursor.fetchall()
    conn.close()
    return enrollments

def delete_enrollment(enrollment_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enrollments WHERE id = ?", (enrollment_id,))
    conn.commit()
    conn.close()
