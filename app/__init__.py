from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database with app
    db.init_app(app)
    
    # Import models to ensure they're registered with SQLAlchemy
    from app.models import event, ticket
    
    # Create tables within application context
    with app.app_context():
        db.create_all()
        # Verify tables were created (optional debug)
        #print("Created tables:", db.engine.table_names())  # For SQLAlchemy <1.4
        # For SQLAlchemy >=1.4 use:
        print("Created tables:", db.metadata.tables.keys())
    
    # Register blueprints
    from app.controllers import event_controller, ticket_controller
    app.register_blueprint(event_controller.bp)
    app.register_blueprint(ticket_controller.bp)
    
    return app