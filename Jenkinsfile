pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Code downloaded from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Docker image build stage'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployment stage'
            }
        }
    }
}