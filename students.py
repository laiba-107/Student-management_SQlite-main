from db import get_db_connection

class StudentManager:
    @staticmethod
    def add_student(first, last, email, dob=None, gender=None, dept_id=None):
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO students (first_name, last_name, email, dob, gender, department_id) VALUES (?, ?, ?, ?, ?, ?)",
                (first, last, email, dob, gender, dept_id)
            )
            conn.commit()
            print("Student added.")

    @staticmethod
    def view_students():
        with get_db_connection() as conn:
            cursor = conn.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows


    @staticmethod
    def update_student(student_id, first=None, last=None, email=None, dob=None, gender=None, dept_id=None):
        with get_db_connection() as conn:
            if first:
                conn.execute("UPDATE students SET first_name = ? WHERE id = ?", (first, student_id))
            if last:
                conn.execute("UPDATE students SET last_name = ? WHERE id = ?", (last, student_id))
            if email:
                conn.execute("UPDATE students SET email = ? WHERE id = ?", (email, student_id))
            if dob:
                conn.execute("UPDATE students SET dob = ? WHERE id = ?", (dob, student_id))
            if gender:
                conn.execute("UPDATE students SET gender = ? WHERE id = ?", (gender, student_id))
            if dept_id == 0:
                conn.execute("UPDATE students SET department_id = NULL WHERE id = ?", (student_id,))
            elif dept_id:
                conn.execute("UPDATE students SET department_id = ? WHERE id = ?", (dept_id, student_id))
            conn.commit()
            print("Student updated.")

    @staticmethod
    def delete_student(student_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            print("Student deleted.")
