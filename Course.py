from db import get_db_connection

class CourseManager:
    @staticmethod
    def add_course(title, credits, dept_id, inst_id=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO courses (title, credits, department_id, instructor_id) VALUES (?, ?, ?, ?)",
                (title, credits, dept_id, inst_id)
            )
            print("Course added.")

    @staticmethod
    def view_courses():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM courses")
            for row in cursor.fetchall():
                print(row)

    @staticmethod
    def update_course(course_id, title=None, credits=None, dept_id=None, inst_id=None):
        with get_db_connection() as conn:
            if title:
                conn.execute("UPDATE courses SET title = ? WHERE id = ?", (title, course_id))
            if credits:
                conn.execute("UPDATE courses SET credits = ? WHERE id = ?", (credits, course_id))
            if dept_id:
                conn.execute("UPDATE courses SET department_id = ? WHERE id = ?", (dept_id, course_id))
            if inst_id == 0:
                conn.execute("UPDATE courses SET instructor_id = NULL WHERE id = ?", (course_id,))
            elif inst_id:
                conn.execute("UPDATE courses SET instructor_id = ? WHERE id = ?", (inst_id, course_id))
            print("Course updated.")

    @staticmethod
    def delete_course(course_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM courses WHERE id = ?", (course_id,))
            print("Course deleted.")
