
# MLOps Flask API

End-to-end MLOps project using Flask, Docker, and AWS EC2 for ML model deployment and API serving.

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Docker
- AWS EC2
- Git & GitHub

---

## Features

- ML model training
- Flask REST API
- Docker containerization
- Cloud deployment on AWS EC2
- Kubernetes-ready architecture

---

## Project Structure

```text
mlops-flask-api/
├── app/
│   └── app.py
├── model/
├── train.py
├── requirements.txt
├── Dockerfile
└── README.md

pip install -r requirements.txt
python train.py
python app/app.py


docker build -t mlops-flask-api .
docker run -d -p 5000:5000 mlops-flask-api

GET  /
POST /predict

Author

Muhammad Raees

GitHub: https://github.com/raeesmalik89-oss
