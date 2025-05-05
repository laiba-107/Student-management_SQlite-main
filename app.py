from flask import Flask, request, jsonify
from students import StudentManager

app = Flask(__name__)

# Create student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    first = data.get("first")
    last = data.get("last")
    email = data.get("email")
    dob = data.get("dob")
    gender = data.get("gender")
    dept_id = data.get("dept_id")

    StudentManager.add_student(first, last, email, dob, gender, dept_id)
    return jsonify({"message": "Student added"}), 201

# Read all students
@app.route("/students", methods=["GET"])
def get_students():
    students = []
    for row in StudentManager.view_students():
        students.append(dict(row))
    return jsonify(students)

# Update student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    StudentManager.update_student(
        student_id,
        first=data.get("first"),
        last=data.get("last"),
        email=data.get("email"),
        dob=data.get("dob"),
        gender=data.get("gender"),
        dept_id=data.get("dept_id")
    )
    return jsonify({"message": "Student updated"})

# Delete student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    StudentManager.delete_student(student_id)
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)
