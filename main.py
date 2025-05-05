from db import initialize_db
from department import DepartmentManager
from Instructor import InstructorManager
from Course import CourseManager
from students import StudentManager
from Enrollment import EnrollmentManager
from fastapi import FastAPI # type: ignore
from api.router import router

app = FastAPI(title="Student Management API")
app.include_router(router)

def department_menu():
    while True:
        print("\nDepartment Management")
        print("1. Add Department")
        print("2. View Departments")
        print("3. Update Department")
        print("4. Delete Department")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter department name: ")
            office = input("Enter office location (optional): ") or None
            DepartmentManager.add_department(name, office)
        elif choice == "2":
            DepartmentManager.view_departments()
        elif choice == "3":
            DepartmentManager.view_departments()
            dept_id = input("Enter department ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            office = input("Enter new office location (leave blank to keep current): ") or None
            DepartmentManager.update_department(dept_id, name, office)
        elif choice == "4":
            DepartmentManager.view_departments()
            dept_id = input("Enter department ID to delete: ")
            DepartmentManager.delete_department(dept_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def instructor_menu():
    while True:
        print("\nInstructor Management")
        print("1. Add Instructor")
        print("2. View Instructors")
        print("3. Update Instructor")
        print("4. Delete Instructor")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter instructor name: ")
            email = input("Enter email: ")
            dept_id = input("Enter department ID (leave blank if none): ") or None
            InstructorManager.add_instructor(name, email, dept_id)
        elif choice == "2":
            InstructorManager.view_instructors()
        elif choice == "3":
            InstructorManager.view_instructors()
            inst_id = input("Enter instructor ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            email = input("Enter new email (leave blank to keep current): ") or None
            dept_id = input("Enter new department ID (0 to remove, leave blank to keep current): ") or None
            InstructorManager.update_instructor(inst_id, name, email, dept_id)
        elif choice == "4":
            InstructorManager.view_instructors()
            inst_id = input("Enter instructor ID to delete: ")
            InstructorManager.delete_instructor(inst_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def course_menu():
    while True:
        print("\nCourse Management")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter course title: ")
            credits = input("Enter credits: ")
            dept_id = input("Enter department ID: ")
            inst_id = input("Enter instructor ID (leave blank if none): ") or None
            CourseManager.add_course(title, credits, dept_id, inst_id)
        elif choice == "2":
            CourseManager.view_courses()
        elif choice == "3":
            CourseManager.view_courses()
            course_id = input("Enter course ID to update: ")
            title = input("Enter new title (leave blank to keep current): ") or None
            credits = input("Enter new credits (leave blank to keep current): ") or None
            dept_id = input("Enter new department ID (leave blank to keep current): ") or None
            inst_id = input("Enter new instructor ID (0 to remove, leave blank to keep current): ") or None
            CourseManager.update_course(course_id, title, credits, dept_id, inst_id)
        elif choice == "4":
            CourseManager.view_courses()
            course_id = input("Enter course ID to delete: ")
            CourseManager.delete_course(course_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu():
    while True:
        print("\nStudent Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            email = input("Enter email: ")
            dob = input("Enter date of birth (YYYY-MM-DD, optional): ") or None
            gender = input("Enter gender (optional): ") or None
            dept_id = input("Enter department ID (optional): ") or None
            StudentManager.add_student(first, last, email, dob, gender, dept_id)
        elif choice == "2":
            StudentManager.view_students()
        elif choice == "3":
            StudentManager.view_students()
            student_id = input("Enter student ID to update: ")
            first = input("Enter new first name (leave blank to keep current): ") or None
            last = input("Enter new last name (leave blank to keep current): ") or None
            email = input("Enter new email (leave blank to keep current): ") or None
            dob = input("Enter new date of birth (YYYY-MM-DD, leave blank to keep current): ") or None
            gender = input("Enter new gender (leave blank to keep current): ") or None
            dept_id = input("Enter new department ID (0 to remove, leave blank to keep current): ") or None
            StudentManager.update_student(student_id, first, last, email, dob, gender, dept_id)
        elif choice == "4":
            StudentManager.view_students()
            student_id = input("Enter student ID to delete: ")
            StudentManager.delete_student(student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def enrollment_menu():
    while True:
        print("\nEnrollment Management")
        print("1. Enroll Student")
        print("2. View Enrollments")
        print("3. Update Grade")
        print("4. Delete Enrollment")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            EnrollmentManager.enroll_student(student_id, course_id)
        elif choice == "2":
            EnrollmentManager.view_enrollments()
        elif choice == "3":
            EnrollmentManager.view_enrollments()
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter new grade: ")
            EnrollmentManager.update_grade(student_id, course_id, grade)
        elif choice == "4":
            EnrollmentManager.view_enrollments()
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            EnrollmentManager.delete_enrollment(student_id, course_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    initialize_db()
    while True:
        print("\nStudent Management System")
        print("1. Manage Departments")
        print("2. Manage Instructors")
        print("3. Manage Courses")
        print("4. Manage Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            department_menu()
        elif choice == "2":
            instructor_menu()
        elif choice == "3":
            course_menu()
        elif choice == "4":
            student_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()