from db import get_db_connection

class InstructorManager:
    @staticmethod
    def add_instructor(name, email, dept_id=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO instructors (name, email, department_id) VALUES (?, ?, ?)",
                (name, email, dept_id)
            )
            print("Instructor added.")

    @staticmethod
    def view_instructors():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM instructors")
            for row in cursor.fetchall():
                print(row)

    @staticmethod
    def update_instructor(inst_id, name=None, email=None, dept_id=None):
        with get_db_connection() as conn:
            if name:
                conn.execute("UPDATE instructors SET name = ? WHERE id = ?", (name, inst_id))
            if email:
                conn.execute("UPDATE instructors SET email = ? WHERE id = ?", (email, inst_id))
            if dept_id == 0:
                conn.execute("UPDATE instructors SET department_id = NULL WHERE id = ?", (inst_id,))
            elif dept_id:
                conn.execute("UPDATE instructors SET department_id = ? WHERE id = ?", (dept_id, inst_id))
            print("Instructor updated.")

    @staticmethod
    def delete_instructor(inst_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM instructors WHERE id = ?", (inst_id,))
            print("Instructor deleted.")
