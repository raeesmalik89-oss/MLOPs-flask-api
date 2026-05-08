
pipeline {
    agent {
    label 'docker-agent'
}

    environment {
        IMAGE_NAME = "mraees1989/mlops-flask-api"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/raeesmalik89-oss/MLOPs-flask-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }

        stage('Restart Kubernetes Deployment') {
            steps {
                sh 'kubectl rollout restart deployment mlops-api'
            }
        }
    }
}
