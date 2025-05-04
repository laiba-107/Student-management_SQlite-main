from db import get_db_connection

def add_student(name, email, major):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, email, major) VALUES (?, ?, ?)", (name, email, major))
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students

def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
