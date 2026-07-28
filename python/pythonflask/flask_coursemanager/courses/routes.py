from flask import Blueprint, jsonify, request
from app import db
from courses.models import Course, Student

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')


def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return make_response_json([c.to_dict() for c in courses])


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    required_fields = ['name', 'code', 'credits', 'department_id']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({'error': f'Missing required fields: {", ".join(missing)}'}), 400

    course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id'],
    )
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict())


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    for field in ('name', 'code', 'credits', 'department_id'):
        if field in data:
            setattr(course, field, data[field])

    db.session.commit()
    return jsonify(course.to_dict())


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return '', 204

@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    course = Course.query.get_or_404(course_id)
    students = [enrollment.student for enrollment in course.enrollments]
    return make_response_json([s.to_dict() for s in students])