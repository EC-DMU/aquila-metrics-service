pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Virtual Enviroment Setup') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Requirements Installation'){
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Jenkins Test') {
            steps {
                sh '. venv/bin/activate && python3 -m pytest tests/jenkins_test.py'
            }
        }
    }  
}