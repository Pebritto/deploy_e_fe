from werkzeug.security import generate_password_hash
from app.models.user import User
from app.extensions import db

class AuthService:
    @staticmethod
    def register_user(user_data):
        try:
            hashed_password = generate_password_hash(user_data['password'])
            new_user = User(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=hashed_password,
                role=user_data.get('role', 'student')
            )
            db.session.add(new_user)
            db.session.commit()
            return {'success': True, 'message': 'User created successfully'}
        except Exception as e:
            return {'success': False, 'message': str(e)}