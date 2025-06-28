from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # student, professor, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    profile_picture = db.Column(db.String(255))
    
    # Relacionamentos
    student_profile = db.relationship('Student', back_populates='user', uselist=False, cascade='all, delete-orphan')
    professor_profile = db.relationship('Professor', back_populates='user', uselist=False, cascade='all, delete-orphan')

class Student(db.Model):
    __tablename__ = 'students'
    
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    enrollment_number = db.Column(db.String(20), unique=True, nullable=False)
    current_semester = db.Column(db.Integer)
    major = db.Column(db.String(100))
    admission_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    
    user = db.relationship('User', back_populates='student_profile')
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')

class Professor(db.Model):
    __tablename__ = 'professors'
    
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    employee_number = db.Column(db.String(20), unique=True, nullable=False)
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))
    
    user = db.relationship('User', back_populates='professor_profile')
    classes = db.relationship('Class', back_populates='professor')