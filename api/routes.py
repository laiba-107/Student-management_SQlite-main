from flask import Blueprint, request, jsonify
from functools import wraps
from .models import Department, Instructor, Course, Student, Enrollment
from datetime import datetime
import logging

api = Blueprint('api', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Error handling decorator
def handle_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyError as e:
            logger.error(f"Missing required field: {str(e)}")
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except ValueError as e:
            logger.error(f"Invalid value: {str(e)}")
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return jsonify({'error': 'An unexpected error occurred'}), 500
    return wrapper

# Validation functions
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

def validate_email(email):
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("Invalid email format")
    return email

# Pagination and filtering parameters
def get_pagination_params():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return page, per_page

# Department Routes
@api.route('/departments', methods=['GET'])
@handle_errors
def get_departments():
    page, per_page = get_pagination_params()
    departments = Department.get_all(page=page, per_page=per_page)
    return jsonify({
        'data': departments,
        'page': page,
        'per_page': per_page,
        'total': Department.count()
    })

@api.route('/departments', methods=['POST'])
@handle_errors
def create_department():
    data = request.get_json()
    if not data.get('name'):
        raise ValueError("Department name is required")
    
    department_id = Department.create(
        name=data['name'],
        office_location=data.get('office_location'),
        budget=data.get('budget'),
        established_date=data.get('established_date')
    )
    logger.info(f"Department created with ID: {department_id}")
    return jsonify({
        'department_id': department_id,
        'message': 'Department created successfully'
    }), 201

@api.route('/departments/<int:department_id>', methods=['GET'])
@handle_errors
def get_department(department_id):
    department = Department.get_by_id(department_id)
    if not department:
        return jsonify({'error': 'Department not found'}), 404
    
    # Include related data
    department['instructors'] = Instructor.get_by_department(department_id)
    department['courses'] = Course.get_by_department(department_id)
    return jsonify(department)

# Enhanced Instructor Routes
@api.route('/instructors', methods=['GET'])
@handle_errors
def get_instructors():
    page, per_page = get_pagination_params()
    department_id = request.args.get('department_id')
    
    if department_id:
        instructors = Instructor.get_by_department(department_id, page, per_page)
    else:
        instructors = Instructor.get_all(page, per_page)
    
    return jsonify({
        'data': instructors,
        'page': page,
        'per_page': per_page,
        'total': Instructor.count(department_id)
    })

@api.route('/instructors', methods=['POST'])
@handle_errors
def create_instructor():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email']
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"{field.replace('_', ' ').title()} is required")
    
    # Validate email
    validate_email(data['email'])
    
    instructor_id = Instructor.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        office=data.get('office'),
        department_id=data.get('department_id'),
        hire_date=data.get('hire_date')
    )
    logger.info(f"Instructor created with ID: {instructor_id}")
    return jsonify({
        'instructor_id': instructor_id,
        'message': 'Instructor created successfully'
    }), 201

# Enhanced Course Routes with Prerequisites
@api.route('/courses', methods=['POST'])
@handle_errors
def create_course():
    data = request.get_json()
    required_fields = ['title', 'credits', 'department_id']
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"{field.replace('_', ' ').title()} is required")
    
    course_id = Course.create(
        code=data.get('code'),
        title=data['title'],
        description=data.get('description'),
        credits=data['credits'],
        department_id=data['department_id'],
        instructor_id=data.get('instructor_id'),
        schedule=data.get('schedule'),
        classroom=data.get('classroom'),
        prerequisites=data.get('prerequisites', [])
    )
    logger.info(f"Course created with ID: {course_id}")
    return jsonify({
        'course_id': course_id,
        'message': 'Course created successfully'
    }), 201

# Enhanced Student Routes with Age Validation
@api.route('/students', methods=['POST'])
@handle_errors
def create_student():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email']
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"{field.replace('_', ' ').title()} is required")
    
    # Validate email
    validate_email(data['email'])
    
    # Validate date if provided
    if data.get('date_of_birth'):
        dob = validate_date(data['date_of_birth'])
        if (datetime.now().year - dob.year) < 16:
            raise ValueError("Student must be at least 16 years old")
    
    student_id = Student.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        address=data.get('address'),
        date_of_birth=data.get('date_of_birth'),
        gender=data.get('gender'),
        enrollment_date=data.get('enrollment_date'),
        department_id=data.get('department_id')
    )
    logger.info(f"Student created with ID: {student_id}")
    return jsonify({
        'student_id': student_id,
        'message': 'Student created successfully'
    }), 201

# Enhanced Enrollment Routes with Grade Validation
@api.route('/enrollments', methods=['POST'])
@handle_errors
def create_enrollment():
    data = request.get_json()
    required_fields = ['student_id', 'course_id']
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"{field.replace('_', ' ').title()} is required")
    
    # Validate grade if provided
    if data.get('grade'):
        grade = data['grade'].upper()
        valid_grades = ['A', 'B', 'C', 'D', 'F', 'W', 'I']
        if grade not in valid_grades:
            raise ValueError(f"Invalid grade. Must be one of: {', '.join(valid_grades)}")
        data['grade'] = grade
    
    enrollment_id = Enrollment.create(
        student_id=data['student_id'],
        course_id=data['course_id'],
        grade=data.get('grade'),
        status=data.get('status', 'active')
    )
    logger.info(f"Enrollment created with ID: {enrollment_id}")
    return jsonify({
        'enrollment_id': enrollment_id,
        'message': 'Enrollment created successfully'
    }), 201

# Search Endpoint
@api.route('/search', methods=['GET'])
@handle_errors
def search():
    query = request.args.get('q', '').strip()
    if len(query) < 2:
        return jsonify({'error': 'Search query must be at least 2 characters'}), 400
    
    results = {
        'students': Student.search(query),
        'courses': Course.search(query),
        'instructors': Instructor.search(query),
        'departments': Department.search(query)
    }
    
    return jsonify(results)

# Bulk Operations
@api.route('/students/bulk', methods=['POST'])
@handle_errors
def create_students_bulk():
    students_data = request.get_json()
    if not isinstance(students_data, list):
        raise ValueError("Expected an array of student data")
    
    created_ids = []
    for student_data in students_data:
        try:
            student_id = Student.create(**student_data)
            created_ids.append(student_id)
        except Exception as e:
            logger.error(f"Error creating student: {str(e)}")
            continue
    
    return jsonify({
        'created_ids': created_ids,
        'message': f'Successfully created {len(created_ids)} students'
    }), 201

# Statistics Endpoint
@api.route('/stats', methods=['GET'])
@handle_errors
def get_stats():
    return jsonify({
        'student_count': Student.count(),
        'course_count': Course.count(),
        'instructor_count': Instructor.count(),
        'department_count': Department.count(),
        'enrollment_count': Enrollment.count(),
        'grade_distribution': Enrollment.grade_distribution(),
        'recent_enrollments': Enrollment.recent(5)
    })