import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from app import app  # noqa: E402


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home():
    response = client().get("/")
    assert response.status_code == 200
    assert b"MLOps Flask API Running" in response.data


def test_predict_returns_valid_class():
    response = client().post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert response.get_json()["prediction"] in (0, 1, 2)
