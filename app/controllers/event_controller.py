from flask import Blueprint, request, jsonify
from app.services.event_service import EventService
from app.utils.response_utils import success, error
from datetime import datetime

bp = Blueprint('events', __name__, url_prefix='/api/events')

@bp.route('/', methods=['GET'])
def get_events():
    events = EventService.get_all_events()
    return success([event.serialize() for event in events])

@bp.route('/', methods=['POST'])
def create_event():
    data = request.get_json()
    try:
        data['date'] = datetime.fromisoformat(data['date'])
        event = EventService.create_event(data)
        return success(event.serialize(), status_code=201)
    except (KeyError, ValueError) as e:
        return error(str(e), 400)

@bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = EventService.get_event_by_id(event_id)
    if not event:
        return error('Event not found', 404)
    return success(event.serialize())