""" 
hatch interview message service app
"""

import logging
from flask import Flask, request
from app.models.db import db, Attachment, Conversation, Message
from flask import current_app as app

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/api/messages/sms", methods=["POST"])
@app.route("/api/webhooks/sms", methods=["POST"])
def create_message():
    """
    Handles POST requests to create a new message with optional attachments.
    """
    data = request.get_json()
    logging.info("Received POST request on /api/messages with data: %s", data)

    attachments_data = data.pop("attachments", [])
    logging.info(data)

    #new_message = Message(**data)
    new_message = Message(frm=data["from"], 
                          to=data["to"], 
                          type=data["type"], 
                          body=data["body"], 
                          timestamp=data["timestamp"])
    
    for attachment_data in attachments_data:
        new_attachment = Attachment(url=attachment_data)
        new_message.attachments.append(new_attachment)
        
    db.session.add(new_message)
    db.session.commit()

    return "OK", 200

@app.route("/api/messages", methods=["POST"])
def sms():
    """
    Handles POST requests to sms endpoint
    """
    data = request.get_json()
    logging.info("Received POST request on %s with data: %s", request.path, data)
    return "OK", 200

@app.route("/api/conversations/", methods=["GET"])
def conversations():
    """
    Handles GET requests to conversations endpoint, returns list of conversations
    """
    data = request.get_json()
    logging.info("Received GET request on %s with data: %s", request.path, data)
    return "OK", 200


@app.route("/api/conversations/<id>/messages", methods=["POST"])
def return_conversation():
    """
    Returns conversation thread for id
    """
    data = request.get_json()
    logging.info("Received GET request on %s for %s with data: %s", request.path, id, data)
    return "OK", 200

#if __name__ == "__main__":
#    app.run(debug=True)
