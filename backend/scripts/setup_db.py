import os
from faker import Faker
from werkzeug.security import generate_password_hash
# from app import create_app
from app.extensions import db
from app.models import User, Student, Professor, Course, Class, Enrollment

# app = create_app()
# app.app_context().push()
fake = Faker('pt_BR')

def create_tables():
    """Cria todas as tabelas no banco de dados"""
    print("🛠️ Criando tabelas...")
    db.drop_all()
    db.create_all()
    print("✅ Tabelas criadas com sucesso!")

def seed_data():
    """Popula o banco com dados iniciais"""
    print("🌱 Populando banco de dados...")
    
    # Admin
    admin = User(
        username='admin',
        email='admin@faculdade.edu',
        password_hash=generate_password_hash('Admin@123'),
        role='admin'
    )
    db.session.add(admin)
    
    # Professores
    professors = []
    for i in range(1, 6):
        user = User(
            username=f'prof{i}',
            email=f'prof{i}@faculdade.edu',
            password_hash=generate_password_hash('Professor@123'),
            role='professor'
        )
        professor = Professor(
            professor_id=user.id,
            employee_number=f"PROF{1000 + i}",
            department=fake.random_element(['TI', 'Matemática', 'Engenharia']),
            position='Professor'
        )
        professors.append(professor)
        db.session.add(user)
        db.session.add(professor)
    
    # Alunos
    students = []
    for i in range(1, 21):
        user = User(
            username=f'aluno{i}',
            email=f'aluno{i}@faculdade.edu',
            password_hash=generate_password_hash('Aluno@123'),
            role='student'
        )
        student = Student(
            student_id=user.id,
            enrollment_number=f"2023{i:03d}",
            current_semester=fake.random_int(1, 8),
            major='Ciência da Computação'
        )
        students.append(student)
        db.session.add(user)
        db.session.add(student)
    
    # Cursos
    courses = [
        Course(code='CC101', name='Introdução à Programação', credits=4),
        Course(code='CC201', name='Estruturas de Dados', credits=5),
        Course(code='CC301', name='Banco de Dados', credits=5)
    ]
    for course in courses:
        db.session.add(course)
    
    db.session.commit()
    
    # Turmas
    classes = []
    for i, course in enumerate(courses):
        class_ = Class(
            course_id=course.course_id,
            professor_id=professors[i].professor_id,
            semester='2023.2',
            schedule={'days': ['Mon', 'Wed'], 'time': '19:00-22:00'},
            max_students=30
        )
        classes.append(class_)
        db.session.add(class_)
    
    db.session.commit()
    
    # Matrículas
    for class_ in classes:
        for student in students[:10]:  # 10 alunos por turma
            enrollment = Enrollment(
                student_id=student.student_id,
                class_id=class_.class_id
            )
            db.session.add(enrollment)
    
    db.session.commit()
    print("✅ Banco populado com sucesso!")

if __name__ == '__main__':
    create_tables()
    seed_data()
    print("\nCredenciais para teste:")
    print("Admin: usuario=admin | senha=Admin@123")
    print("Professor: usuario=prof1 a prof5 | senha=Professor@123")
    print("Aluno: usuario=aluno1 a aluno20 | senha=Aluno@123")