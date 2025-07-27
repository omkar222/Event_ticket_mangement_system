# Import all controllers to make them available when the package is imported
from .event_controller import bp as event_bp
from .ticket_controller import bp as ticket_bp

__all__ = ['event_bp', 'ticket_bp']