from db import get_db_connection
import sqlite3

class EnrollmentManager:
    @staticmethod
    def add_enrollment(student_id, course_id, grade=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
                (student_id, course_id, grade)
            )
            conn.commit()

    @staticmethod
    def view_enrollments():
        with get_db_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT 
                    e.id as enrollment_id,
                    e.student_id,
                    e.course_id,
                    e.grade,
                    s.first_name || ' ' || s.last_name AS student_name,
                    c.title AS course_title,
                    c.credits,
                    d.name AS department_name,
                    i.first_name || ' ' || i.last_name AS instructor_name
                FROM enrollments e
                JOIN students s ON e.student_id = s.id
                JOIN courses c ON e.course_id = c.id
                JOIN departments d ON c.department_id = d.id
                JOIN instructors i ON c.instructor_id = i.id
            """)
            return cursor.fetchall()

    @staticmethod
    def update_enrollment(enrollment_id, grade=None):
        with get_db_connection() as conn:
            conn.execute(
                "UPDATE enrollments SET grade = ? WHERE id = ?",
                (grade, enrollment_id)
            )
            conn.commit()

    @staticmethod
    def delete_enrollment(enrollment_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM enrollments WHERE id = ?", (enrollment_id,))
            conn.commit()