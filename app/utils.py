from typing import List
from app.models.db import Attachment

def add_attachments(attachments_data: List[str]) -> List[Attachment]:
    """
    given list of strings from json, return a list of attachment objects
    """

    if not isinstance(attachments_data, List):
        raise TypeError("attachments not a list.")

    attachments_list = []

    for attachment_url in attachments_data:
        if isinstance(attachment_url, str):
            attachments_list.append(Attachment(url=attachment_url))
        else:
            raise AttributeError("attachment url can not be read")

    return attachments_list
