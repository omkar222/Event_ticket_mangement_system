from datetime import datetime
from app.models.ticket import Ticket
from app.services.token_service import TokenService
from app import db

class TicketService:
    @staticmethod
    def generate_tickets(event_id, quantity):
        tickets = []
        for _ in range(quantity):
            ticket = Ticket(
                token=TokenService.generate_token(),
                event_id=event_id
            )
            tickets.append(ticket)
            db.session.add(ticket)
        db.session.commit()
        return tickets

    @staticmethod
    def redeem_ticket(token):
        ticket = Ticket.query.filter_by(token=token).first()
        if not ticket:
            return None
        
        if not ticket.is_redeemed:
            ticket.is_redeemed = True
            ticket.redeemed_at = datetime.utcnow()
            db.session.commit()
        
        return ticket
    @staticmethod
    def get_ticket_by_token(token):
        """Get ticket details without redeeming it"""
        ticket = Ticket.query.filter_by(token=token).first()
        if not ticket:
            raise ValueError("Ticket not found")
        return ticket