""" 
hatch interview message service app
"""

import logging
from typing import List
from flask import Flask, request, abort, jsonify
from app.models.db import db, Attachment, Message, check_for_thread, threads, conversation
from flask import current_app as app
from app.utils import add_attachments

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/api/messages/sms", methods=["POST"])
@app.route("/api/webhooks/sms", methods=["POST"])
def create_message():
    """
    Handles POST requests to create a new message with optional attachments.
    """

    data = request.get_json()
    logging.info(data)

    new_message = Message(frm=data["from"], 
                    to=data["to"], 
                    type=data["type"], 
                    body=data["body"], 
                    timestamp=data["timestamp"])

    # Optional

    new_message.threadcode = check_for_thread(new_message.to,new_message.frm)

    try:

        attachments_data = data.pop("attachments", [])

        if attachments_data:
            new_message.attachments = add_attachments(attachments_data)

        if "messaging_provider_id" in data:
            new_message.messaging_provider_id=data["messaging_provider_id"],

    except (TypeError, AttributeError):
        abort(400, description="bad request")

    db.session.add(new_message)
    db.session.commit()

    return "OK", 200

@app.route("/api/messages/email", methods=["POST"])
@app.route("/api/webhooks/email", methods=["POST"])
def sms():
    """
    Handles POST requests to sms endpoint
    """

    data = request.get_json()
    logging.info(data)

    new_email = Message(frm=data["from"], 
                    to=data["to"], 
                    type="email", 
                    body=data["body"], 
                    timestamp=data["timestamp"])

    new_email.threadcode = check_for_thread(new_email.to,new_email.frm)

    try:

        attachments_data = data.pop("attachments", [])

        if attachments_data:
            new_email.attachments = add_attachments(attachments_data)

        if "xillio_id" in data:
            new_email.xillio_id=data["xillio_id"],

    except (TypeError, AttributeError):
        abort(400, description="bad request")

    db.session.add(new_email)
    db.session.commit()

    logging.info("Received POST request on %s with data: %s", request.path, data)

    return "OK", 200

@app.route("/api/conversations/", methods=["GET"])
def conversations():
    """
    Handles GET requests to conversations endpoint, returns list of conversations
    """

    data = request.get_json()
    logging.info("Received GET request on %s with data: %s", request.path, data)

    return jsonify(threads()), 200


@app.route("/api/conversations/<id:str>/messages", methods=["POST"])
def return_conversation():
    """
    Returns conversation thread for id
    """
    data = request.get_json()
    logging.info("Received GET request on %s for %s with data: %s", request.path, id, data)

    return jsonify(conversation(id)), 200
