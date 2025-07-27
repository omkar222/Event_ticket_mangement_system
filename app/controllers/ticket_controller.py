from flask import Blueprint, request, jsonify
from app.services.ticket_service import TicketService
from app.utils.response_utils import success, error

bp = Blueprint('tickets', __name__, url_prefix='/api/tickets')

@bp.route('/<int:event_id>/generate', methods=['POST'])
def generate_tickets(event_id):
    data = request.get_json()
    quantity = data.get('quantity', 1)
    
    if not isinstance(quantity, int) or quantity < 1:
        return error('Quantity must be a positive integer', 400)
    
    tickets = TicketService.generate_tickets(event_id, quantity)
    return success([ticket.serialize() for ticket in tickets], status_code=201)

@bp.route('/<string:token>/redeem', methods=['POST'])
def redeem_ticket(token):
    ticket = TicketService.redeem_ticket(token)
    if not ticket:
        return error('Ticket not found', 404)
    return success(ticket.serialize())

@bp.route('/<string:token>', methods=['GET'])
def get_ticket(token):
    try:
        ticket = TicketService.get_ticket_by_token(token)
        return success(ticket.serialize())
    except ValueError as e:
        return error(str(e), 404)