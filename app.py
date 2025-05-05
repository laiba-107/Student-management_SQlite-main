from flask import Flask, request, jsonify, render_template
from students import StudentManager
from department import DepartmentManager
from Course import CourseManager
from Instructor import InstructorManager
from Enrollment import EnrollmentManager
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# if __name__ == "__main__":
#     app.run(debug=True)


# ------------------- STUDENTS -------------------
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    StudentManager.add_student(
        data.get("first"), data.get("last"), data.get("email"),
        data.get("dob"), data.get("gender"), data.get("dept_id")
    )
    return jsonify({"message": "Student added"}), 201

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify([dict(row) for row in StudentManager.view_students()])

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

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    StudentManager.delete_student(student_id)
    return jsonify({"message": "Student deleted"})

# ------------------- DEPARTMENTS -------------------
@app.route("/departments", methods=["POST"])
def add_department():
    data = request.get_json()
    DepartmentManager.add_department(data.get("name"))
    return jsonify({"message": "Department added"}), 201

@app.route("/departments", methods=["GET"])
def get_departments():
    return jsonify([dict(row) for row in DepartmentManager.view_departments()])

@app.route("/departments/<int:dept_id>", methods=["PUT"])
def update_department(dept_id):
    data = request.get_json()
    DepartmentManager.update_department(dept_id, data.get("name"))
    return jsonify({"message": "Department updated"})

@app.route("/departments/<int:dept_id>", methods=["DELETE"])
def delete_department(dept_id):
    DepartmentManager.delete_department(dept_id)
    return jsonify({"message": "Department deleted"})

# ------------------- COURSES -------------------
@app.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json()
    CourseManager.add_course(data.get("name"), data.get("dept_id"))
    return jsonify({"message": "Course added"}), 201

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify([dict(row) for row in CourseManager.view_courses()])

@app.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()
    CourseManager.update_course(course_id, data.get("name"), data.get("dept_id"))
    return jsonify({"message": "Course updated"})

@app.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    CourseManager.delete_course(course_id)
    return jsonify({"message": "Course deleted"})

# ------------------- INSTRUCTORS -------------------
@app.route("/instructors", methods=["POST"])
def add_instructor():
    data = request.get_json()
    InstructorManager.add_instructor(
        data.get("first"), data.get("last"), data.get("email"),
        data.get("dob"), data.get("gender"), data.get("dept_id")
    )
    return jsonify({"message": "Instructor added"}), 201

@app.route("/instructors", methods=["GET"])
def get_instructors():
    return jsonify([dict(row) for row in InstructorManager.view_instructors()])

@app.route("/instructors/<int:instructor_id>", methods=["PUT"])
def update_instructor(instructor_id):
    data = request.get_json()
    InstructorManager.update_instructor(
        instructor_id,
        first=data.get("first"),
        last=data.get("last"),
        email=data.get("email"),
        dob=data.get("dob"),
        gender=data.get("gender"),
        dept_id=data.get("dept_id")
    )
    return jsonify({"message": "Instructor updated"})

@app.route("/instructors/<int:instructor_id>", methods=["DELETE"])
def delete_instructor(instructor_id):
    InstructorManager.delete_instructor(instructor_id)
    return jsonify({"message": "Instructor deleted"})

# ------------------- ENROLLMENTS -------------------
@app.route("/enrollments", methods=["POST"])
def add_enrollment():
    data = request.get_json()
    if not data or 'student_id' not in data or 'course_id' not in data:
        return jsonify({"error": "student_id and course_id are required"}), 400
    
    try:
        EnrollmentManager.add_enrollment(
            student_id=data["student_id"],
            course_id=data["course_id"],
            grade=data.get("grade")
        )
        return jsonify({"message": "Enrollment added successfully"}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": "Invalid student_id or course_id"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/enrollments", methods=["GET"])
def get_enrollments():
    try:
        enrollments = EnrollmentManager.view_enrollments()
        return jsonify([dict(row) for row in enrollments])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/enrollments/<int:enrollment_id>", methods=["PUT"])
def update_enrollment(enrollment_id):
    data = request.get_json()
    if "grade" not in data:
        return jsonify({"error": "grade is required"}), 400
    
    try:
        EnrollmentManager.update_enrollment(
            enrollment_id=enrollment_id,
            grade=data["grade"]
        )
        return jsonify({"message": "Enrollment updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/enrollments/<int:enrollment_id>", methods=["DELETE"])
def delete_enrollment(enrollment_id):
    try:
        EnrollmentManager.delete_enrollment(enrollment_id)
        return jsonify({"message": "Enrollment deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------- MAIN -------------------
if __name__ == "__main__":
    app.run(debug=True)
