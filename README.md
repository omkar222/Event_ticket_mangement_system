# Event Ticket Management System
A complete **Event Ticket Management System** with REST API backend (Flask) and modern UI (Streamlit) following Object-Oriented Programming principles.

## Features

- 🎭 **Event Management**
  - Create, view, and manage events
  - Date/time and location tracking
- 🎟️ **Ticket System**
  - Generate unique ticket tokens
  - Track redemption status
- 💻 **Dual Interface**
  - REST API for developers
  - Streamlit UI for end-users
- 🏗️ **Clean Architecture**
  - Proper separation of concerns
  - SOLID principles applied
  - Easy to maintain and extend

## System Architecture

```
event_ticket_api/
├── app/                       # Core application
│   ├── controllers/           # API endpoints
│   ├── models/                # Database models
│   ├── services/              # Business logic
│   ├── utils/                 # Helper functions
│   └── __init__.py            # App factory
├── streamlit_app.py           # Modern web UI
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## Tech Stack

| Component       | Technology |
|----------------|------------|
| Backend        | Flask      |
| Database ORM   | SQLAlchemy |
| Frontend       | Streamlit  |
| Authentication | -          |
| Deployment     | Docker     |

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/yourrepo/event-ticket-system.git
   cd event-ticket-system
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Update `config.py` with your PostgreSQL credentials
   - Or use SQLite for development

## Running the System

### Backend API
```bash
flask run
```
- API docs available at `http://localhost:5000`

### Streamlit UI
```bash
streamlit run streamlit_app.py
```
- Access UI at `http://localhost:8501`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/events` | POST | Create new event |
| `/api/events` | GET | List all events |
| `/api/tickets/{event_id}/generate` | POST | Generate tickets |
| `/api/tickets/{token}/redeem` | POST | Redeem ticket |


## Development

1. **Database migrations**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

2. **Testing**
   ```bash
   pytest tests/
   ```

## Deployment

1. **Docker setup**
   ```bash
   docker-compose up -d
   ```

2. **Production considerations**
   - Use Gunicorn for Flask
   - Configure proper secret keys
   - Set up PostgreSQL connection pooling

## Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request
