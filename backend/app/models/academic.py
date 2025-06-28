from datetime import datetime
from app.extensions import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    course_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(100))
    
    classes = db.relationship('Class', back_populates='course')

class Class(db.Model):
    __tablename__ = 'classes'
    
    class_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.professor_id'), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    schedule = db.Column(db.JSON, nullable=False)  # {days: ["Mon", "Wed"], time: "14:00-15:30"}
    room = db.Column(db.String(50))
    max_students = db.Column(db.Integer)
    
    course = db.relationship('Course', back_populates='classes')
    professor = db.relationship('Professor', back_populates='classes')
    enrollments = db.relationship('Enrollment', back_populates='class_')

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')
    final_grade = db.Column(db.Numeric(4, 2))
    
    student = db.relationship('Student', back_populates='enrollments')
    class_ = db.relationship('Class', back_populates='enrollments')