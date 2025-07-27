# Import all models to ensure they're registered with SQLAlchemy
from .event import Event
from .ticket import Ticket

__all__ = ['Event', 'Ticket']