from db import get_db_connection

class EnrollmentManager:
    @staticmethod
    def enroll_student(student_id, course_id):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id)
            )
            conn.commit()
            print("Student enrolled.")

    @staticmethod
    def view_enrollments():
        with get_db_connection() as conn:
            cursor = conn.execute("""
                SELECT enrollments.*, 
                       students.first_name || ' ' || students.last_name AS student_name,
                       courses.course_name
                FROM enrollments
                LEFT JOIN students ON enrollments.student_id = students.id
                LEFT JOIN courses ON enrollments.course_id = courses.id
            """)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows

    @staticmethod
    def delete_enrollment(enrollment_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM enrollments WHERE id = ?", (enrollment_id,))
            conn.commit()
            print("Enrollment deleted.")
