from app.models.event import Event
from app import db

class EventService:
    @staticmethod
    def create_event(data):
        event = Event(
            name=data['name'],
            description=data.get('description'),
            date=data['date'],
            location=data.get('location')
        )
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def get_all_events():
        return Event.query.all()

    @staticmethod
    def get_event_by_id(event_id):
        return Event.query.get(event_id)