from db import get_db_connection

def add_instructor(name, email, department_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Instructors (name, email, department_id) VALUES (?, ?, ?)", (name, email, department_id))
    conn.commit()
    conn.close()

def get_all_instructors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Instructors")
    instructors = cursor.fetchall()
    conn.close()
    return instructors

def delete_instructor(instructor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Instructors WHERE id = ?", (instructor_id,))
    conn.commit()
    conn.close()
