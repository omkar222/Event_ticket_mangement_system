import os

class Config:
    SECRET_KEY = 'dev'  # Only for local development!
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Omkar222@localhost:5432/event_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False