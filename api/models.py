from db import get_db_connection

class Department:
    @staticmethod
    def create(name, office_location=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Department (name, office_location) VALUES (?, ?)",
                (name, office_location)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Department")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(department_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Department WHERE department_id = ?", (department_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def update(department_id, name=None, office_location=None):
        updates = []
        params = []
        
        if name:
            updates.append("name = ?")
            params.append(name)
        if office_location is not None:
            updates.append("office_location = ?")
            params.append(office_location)
        
        if updates:
            params.append(department_id)
            with get_db_connection() as conn:
                cursor = conn.cursor()
                query = f"UPDATE Department SET {', '.join(updates)} WHERE department_id = ?"
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        return 0

    @staticmethod
    def delete(department_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Department WHERE department_id = ?", (department_id,))
            conn.commit()
            return cursor.rowcount


class Instructor:
    @staticmethod
    def create(name, email, department_id=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Instructor (name, email, department_id) VALUES (?, ?, ?)",
                (name, email, department_id)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT i.*, d.name as department_name 
                FROM Instructor i
                LEFT JOIN Department d ON i.department_id = d.department_id
            """)
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(instructor_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT i.*, d.name as department_name 
                FROM Instructor i
                LEFT JOIN Department d ON i.department_id = d.department_id
                WHERE i.instructor_id = ?
            """, (instructor_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def update(instructor_id, name=None, email=None, department_id=None):
        updates = []
        params = []
        
        if name:
            updates.append("name = ?")
            params.append(name)
        if email:
            updates.append("email = ?")
            params.append(email)
        if department_id is not None:  # Can be None to remove association
            updates.append("department_id = ?")
            params.append(department_id)
        
        if updates:
            params.append(instructor_id)
            with get_db_connection() as conn:
                cursor = conn.cursor()
                query = f"UPDATE Instructor SET {', '.join(updates)} WHERE instructor_id = ?"
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        return 0

    @staticmethod
    def delete(instructor_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Instructor WHERE instructor_id = ?", (instructor_id,))
            conn.commit()
            return cursor.rowcount


class Course:
    @staticmethod
    def create(title, credits, department_id, instructor_id=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Course (title, credits, department_id, instructor_id) VALUES (?, ?, ?, ?)",
                (title, credits, department_id, instructor_id)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.*, d.name as department_name, i.name as instructor_name
                FROM Course c
                JOIN Department d ON c.department_id = d.department_id
                LEFT JOIN Instructor i ON c.instructor_id = i.instructor_id
            """)
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(course_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.*, d.name as department_name, i.name as instructor_name
                FROM Course c
                JOIN Department d ON c.department_id = d.department_id
                LEFT JOIN Instructor i ON c.instructor_id = i.instructor_id
                WHERE c.course_id = ?
            """, (course_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def update(course_id, title=None, credits=None, department_id=None, instructor_id=None):
        updates = []
        params = []
        
        if title:
            updates.append("title = ?")
            params.append(title)
        if credits:
            updates.append("credits = ?")
            params.append(credits)
        if department_id is not None:
            updates.append("department_id = ?")
            params.append(department_id)
        if instructor_id is not None:  # Can be None to remove instructor
            updates.append("instructor_id = ?")
            params.append(instructor_id)
        
        if updates:
            params.append(course_id)
            with get_db_connection() as conn:
                cursor = conn.cursor()
                query = f"UPDATE Course SET {', '.join(updates)} WHERE course_id = ?"
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        return 0

    @staticmethod
    def delete(course_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Course WHERE course_id = ?", (course_id,))
            conn.commit()
            return cursor.rowcount


class Student:
    @staticmethod
    def create(first_name, last_name, email, date_of_birth=None, gender=None, department_id=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Student 
                (first_name, last_name, email, date_of_birth, gender, department_id) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (first_name, last_name, email, date_of_birth, gender, department_id)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.*, d.name as department_name
                FROM Student s
                LEFT JOIN Department d ON s.department_id = d.department_id
            """)
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(student_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.*, d.name as department_name
                FROM Student s
                LEFT JOIN Department d ON s.department_id = d.department_id
                WHERE s.student_id = ?
            """, (student_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def update(student_id, first_name=None, last_name=None, email=None, 
              date_of_birth=None, gender=None, department_id=None):
        updates = []
        params = []
        
        if first_name:
            updates.append("first_name = ?")
            params.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            params.append(last_name)
        if email:
            updates.append("email = ?")
            params.append(email)
        if date_of_birth is not None:
            updates.append("date_of_birth = ?")
            params.append(date_of_birth)
        if gender is not None:
            updates.append("gender = ?")
            params.append(gender)
        if department_id is not None:  # Can be None to remove department
            updates.append("department_id = ?")
            params.append(department_id)
        
        if updates:
            params.append(student_id)
            with get_db_connection() as conn:
                cursor = conn.cursor()
                query = f"UPDATE Student SET {', '.join(updates)} WHERE student_id = ?"
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        return 0

    @staticmethod
    def delete(student_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Student WHERE student_id = ?", (student_id,))
            conn.commit()
            return cursor.rowcount


class Enrollment:
    @staticmethod
    def create(student_id, course_id, grade=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Enrollment 
                (student_id, course_id, grade) 
                VALUES (?, ?, ?)""",
                (student_id, course_id, grade)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT e.*, 
                       s.first_name || ' ' || s.last_name as student_name,
                       c.title as course_title
                FROM Enrollment e
                JOIN Student s ON e.student_id = s.student_id
                JOIN Course c ON e.course_id = c.course_id
            """)
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(enrollment_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT e.*, 
                       s.first_name || ' ' || s.last_name as student_name,
                       c.title as course_title
                FROM Enrollment e
                JOIN Student s ON e.student_id = s.student_id
                JOIN Course c ON e.course_id = c.course_id
                WHERE e.enrollment_id = ?
            """, (enrollment_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def update(enrollment_id, grade=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Enrollment SET grade = ? WHERE enrollment_id = ?",
                (grade, enrollment_id)
            )
            conn.commit()
            return cursor.rowcount

    @staticmethod
    def delete(enrollment_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Enrollment WHERE enrollment_id = ?", (enrollment_id,))
            conn.commit()
            return cursor.rowcount