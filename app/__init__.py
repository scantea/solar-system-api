from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    # Connects db and migrate to our Flask app,
    # using the package's recommended syntax
    # db and migrate are initialized
    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.planet import Planet
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)
    return app
