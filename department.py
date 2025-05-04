from db import get_db_connection

class DepartmentManager:
    @staticmethod
    def add_department(name, office):
        with get_db_connection() as conn:
            conn.execute("INSERT INTO departments (name, office) VALUES (?, ?)", (name, office))
            print("Department added.")

    @staticmethod
    def view_departments():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM departments")
            for row in cursor.fetchall():
                print(row)

    @staticmethod
    def update_department(dept_id, name=None, office=None):
        with get_db_connection() as conn:
            if name:
                conn.execute("UPDATE departments SET name = ? WHERE id = ?", (name, dept_id))
            if office:
                conn.execute("UPDATE departments SET office = ? WHERE id = ?", (office, dept_id))
            print("Department updated.")

    @staticmethod
    def delete_department(dept_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM departments WHERE id = ?", (dept_id,))
            print("Department deleted.")
