pipeline {
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python dev.py'
            }
        }
        stage('Promote') {
            steps {
                sh 'python --version'
            }
        }   
    }
}

