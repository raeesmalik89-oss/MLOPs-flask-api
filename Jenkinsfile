
pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/raeesmalik89-oss/MLOPs-flask-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-flask-api .'
            }
        }

        stage('Check Kubernetes') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }
}
