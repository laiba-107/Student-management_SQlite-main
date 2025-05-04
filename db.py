import sqlite3

def get_db_connection():
    return sqlite3.connect("student_management.db")

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            office TEXT
        )
    """)

    # Create Instructors table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instructors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES Departments(id)
        )
    """)

    # Create Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            major TEXT
        )
    """)

    # Create Courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT UNIQUE,
            instructor_id INTEGER,
            department_id INTEGER,
            FOREIGN KEY(instructor_id) REFERENCES Instructors(id),
            FOREIGN KEY(department_id) REFERENCES Departments(id)
        )
    """)

    # Create Enrollments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            grade TEXT,
            FOREIGN KEY(student_id) REFERENCES Students(id),
            FOREIGN KEY(course_id) REFERENCES Courses(id)
        )
    """)

    conn.commit()
    conn.close()
