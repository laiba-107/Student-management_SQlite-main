from db import get_db_connection

class EnrollmentManager:
    @staticmethod
    def enroll_student(student_id, course_id):
        with get_db_connection() as conn:
            conn.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            print("Student enrolled in course.")

    @staticmethod
    def view_enrollments():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM enrollments")
            for row in cursor.fetchall():
                print(row)

    @staticmethod
    def delete_enrollment(enrollment_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM enrollments WHERE id = ?", (enrollment_id,))
            print("Enrollment deleted.")
