"""
Unit tests for file_uploader.py
"""


def test_home(test_client):
    """ Unit test for home() """
    response = test_client.get("/")
    assert response.status_code == 200


def test_directly_process(test_client):
    """ Unit test for directly accessing () """
    response = test_client.get("/processor")
    assert response.status_code == 400


def test_proper_file(test_client):
    """ Unit test of processing a proper file. """
    filename = "one_row.csv"
    data = {
        "file": (open("tests/files/" + filename, "rb"), filename)
    }
    response = test_client.post("/processor", data=data)
    assert response.status_code == 201


def test_text_file(test_client):
    """ Unit test of processing a text file. """
    filename = "samp.txt"
    data = {
        "file": (open("tests/files/" + filename, "rb"), filename)
    }
    response = test_client.post("/processor", data=data)
    assert response.status_code == 400


def test_empty_file(test_client):
    """ Unit test of processing an empty file. """
    filename = "empty_file.csv"
    data = {
        "file": (open("tests/files/" + filename, "rb"), filename)
    }
    response = test_client.post("/processor", data=data)
    assert response.status_code == 400


def test_invalid_file(test_client):
    """ Unit test of processing an invalid csv file. """
    filename = "base_data.csv"
    data = {
        "file": (open("tests/files/" + filename, "rb"), filename)
    }
    response = test_client.post("/processor", data=data)
    assert response.status_code == 400


def test_upload_nothing(test_client):
    """ Unit test for not uploading any file. """
    data = {
        "file": (None, "")
    }
    response = test_client.post("/processor", data=data)
    assert response.status_code == 400
