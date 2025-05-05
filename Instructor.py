from db import get_db_connection

class InstructorManager:
    @staticmethod
    def add_instructor(first, last, email, dept_id=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO instructors (first, last, email, department_id) VALUES (?, ?, ?, ?)",
                (first, last, email, dept_id)
            )
            conn.commit()
            print("Instructor added.")

    @staticmethod
    def view_instructors():
        with get_db_connection() as conn:
            cursor = conn.execute("""
                SELECT instructors.*, departments.name AS department_name
                FROM instructors
                LEFT JOIN departments ON instructors.department_id = departments.id
            """)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows

    @staticmethod
    def update_instructor(instructor_id, first=None, last=None, email=None, dept_id=None):
        with get_db_connection() as conn:
            if first:
                conn.execute("UPDATE instructors SET first = ? WHERE id = ?", (first, instructor_id))
            if last:
                conn.execute("UPDATE instructors SET last = ? WHERE id = ?", (last, instructor_id))
            if email:
                conn.execute("UPDATE instructors SET email = ? WHERE id = ?", (email, instructor_id))
            if dept_id == 0:
                conn.execute("UPDATE instructors SET department_id = NULL WHERE id = ?", (instructor_id,))
            elif dept_id:
                conn.execute("UPDATE instructors SET department_id = ? WHERE id = ?", (dept_id, instructor_id))
            conn.commit()
            print("Instructor updated.")

    @staticmethod
    def delete_instructor(instructor_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM instructors WHERE id = ?", (instructor_id,))
            conn.commit()
            print("Instructor deleted.")
