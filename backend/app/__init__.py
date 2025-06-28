from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes import auth, academic, gamification, ai_tutor
    app.register_blueprint(auth.bp)
    app.register_blueprint(academic.bp)
    app.register_blueprint(gamification.bp)
    app.register_blueprint(ai_tutor.bp)

    return app