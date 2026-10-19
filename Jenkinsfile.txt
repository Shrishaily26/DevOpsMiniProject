pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Shrishaily26/DevOpsMiniProject.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }
    }
}