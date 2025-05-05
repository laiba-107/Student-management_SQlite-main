from db import get_db_connection

class CourseManager:
    @staticmethod
    def add_course(course_name, credits, dept_id=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO courses (course_name, credits, department_id) VALUES (?, ?, ?)",
                (course_name, credits, dept_id)
            )
            conn.commit()
            print("Course added.")

    @staticmethod
    def view_courses():
        with get_db_connection() as conn:
            cursor = conn.execute("""
                SELECT courses.*, departments.name AS department_name
                FROM courses
                LEFT JOIN departments ON courses.department_id = departments.id
            """)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows

    @staticmethod
    def update_course(course_id, course_name=None, credits=None, dept_id=None):
        with get_db_connection() as conn:
            if course_name:
                conn.execute("UPDATE courses SET course_name = ? WHERE id = ?", (course_name, course_id))
            if credits is not None:
                conn.execute("UPDATE courses SET credits = ? WHERE id = ?", (credits, course_id))
            if dept_id == 0:
                conn.execute("UPDATE courses SET department_id = NULL WHERE id = ?", (course_id,))
            elif dept_id:
                conn.execute("UPDATE courses SET department_id = ? WHERE id = ?", (dept_id, course_id))
            conn.commit()
            print("Course updated.")

    @staticmethod
    def delete_course(course_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM courses WHERE id = ?", (course_id,))
            conn.commit()
            print("Course deleted.")
