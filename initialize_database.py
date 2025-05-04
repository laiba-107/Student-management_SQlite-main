import sqlite3

def initialize_database():
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()

    # Departments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        office TEXT
    )
    """)

    # Instructors
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instructors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
    """)

    # Students
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        dob TEXT,
        gender TEXT,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
    """)

    # Courses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        credits INTEGER,
        department_id INTEGER,
        instructor_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id),
        FOREIGN KEY (instructor_id) REFERENCES instructors(id)
    )
    """)

    # Enrollments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized: student_management.db")

if __name__ == "__main__":
    initialize_database()
