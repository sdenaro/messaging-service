"""
Static config file
"""

class Config:
    """
    Application Config Settings
    """
    SQLALCHEMY_DATABASE_URI = "postgresql://messaging_user:messaging_password@localhost:5432/messaging_service"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
