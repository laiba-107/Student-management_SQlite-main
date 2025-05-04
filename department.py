from db import get_db_connection

def add_department(name, office):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Departments (name, office) VALUES (?, ?)", (name, office))
    conn.commit()
    conn.close()

def get_all_departments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Departments")
    departments = cursor.fetchall()
    conn.close()
    return departments

def delete_department(department_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Departments WHERE id = ?", (department_id,))
    conn.commit()
    conn.close()
