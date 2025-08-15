"""
entry point to run Flask app
"""

from app import create_app

app = create_app()

print("startup")

#with app.app_context():
#    db.create_all()
#    db.commit()
#    print("Database created!")
