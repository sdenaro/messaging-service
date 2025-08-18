"""
entry point to run Flask app
"""

from app import create_app
app = create_app()
app.run(port=8080)

print("startup")
