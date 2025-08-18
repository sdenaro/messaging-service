import pytest
from app.utils import add_attachments
from app.models.db import Attachment

def test_add_attachments_valid_data():
    """
    Tests that add_attachments returns a list of Attachment objects when valid data is passed.
    """
    attachments_data = ["http://example.com/image.png", "http://example.com/document.pdf"]
    attachments = add_attachments(attachments_data)
    assert len(attachments) == 2
    for attachment in attachments:
        assert isinstance(attachment, Attachment)
    assert attachments[0].url == "http://example.com/image.png"
    assert attachments[1].url == "http://example.com/document.pdf"

def test_add_no_attachments_valid_data():
    """
    Tests that add_attachments returns a list of Attachment objects when valid data is passed.
    """
    attachments_data = []
    attachments = add_attachments(attachments_data)
    assert len(attachments) == 0
    for attachment in attachments:
        assert isinstance(attachment, Attachment)

def test_add_attachments_invalid_data_type():
    """
    Tests that add_attachments raises a TypeError when invalid data type is passed.
    """
    attachments_data = "not a list"
    with pytest.raises(TypeError):
        add_attachments(attachments_data)

def test_add_attachments_list_with_invalid_data_type():
    """
    Tests that add_attachments raises an exception when a list with invalid data types is passed.
    """
    attachments_data = [123, {"url": "http://example.com"}]
    with pytest.raises(AttributeError):
        add_attachments(attachments_data)
