pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-mini-project .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop devops-container || true'
                sh 'docker rm devops-container || true'
            }
        }

        stage('Deploy New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name devops-container devops-mini-project'
            }
        }
    }
}