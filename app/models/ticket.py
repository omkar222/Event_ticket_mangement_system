from datetime import datetime
from app import db

class Ticket(db.Model):
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(64), unique=True, nullable=False)
    is_redeemed = db.Column(db.Boolean, default=False)
    redeemed_at = db.Column(db.DateTime)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'token': self.token,
            'is_redeemed': self.is_redeemed,
            'redeemed_at': self.redeemed_at.isoformat() if self.redeemed_at else None,
            'event_id': self.event_id,
            'created_at': self.created_at.isoformat()
        }