pipeline {
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install pre-reqs') {
            steps {
                // sh 'python -m pip install requests'
                sh """
                python3 -m venv env
                source ./env/bin/activate 
                python -m pip install requests
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                source ./env/bin/activate 
                python webapp/unit.py
                """
            }
        }
        stage('Promote') {
            steps {
                sh 'python --version'
            }
        }   
    }
}
