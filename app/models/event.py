from datetime import datetime
from app import db

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date.isoformat(),
            'location': self.location,
            'created_at': self.created_at.isoformat()
        }