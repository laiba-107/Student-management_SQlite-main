from db import get_db_connection

class DepartmentManager:
    @staticmethod
    def add_department(name):
        with get_db_connection() as conn:
            conn.execute("INSERT INTO departments (name) VALUES (?)", (name,))
            conn.commit()
            print("Department added.")

    @staticmethod
    def view_departments():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM departments")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows

    @staticmethod
    def update_department(department_id, name):
        with get_db_connection() as conn:
            conn.execute("UPDATE departments SET name = ? WHERE id = ?", (name, department_id))
            conn.commit()
            print("Department updated.")

    @staticmethod
    def delete_department(department_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM departments WHERE id = ?", (department_id,))
            conn.commit()
            print("Department deleted.")
