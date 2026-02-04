pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t metrics-api:$BUILD_NUMBER .'
            }
        }
        stage('Test Application'){
            steps {
                sh 'docker run --rm metrics-api:$BUILD_NUMBER python -m pytest /api | tee test_log.log'
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'docker stop metrics-container || true'
                sh 'docker rm metrics-container || true'
                sh 'docker run -d -p 5050:5050 --name metrics-container metrics-api:$BUILD_NUMBER'
            }
        }
    }  
    post {
        always {
            archiveArtifacts artifacts: 'test_log.log', allowEmptyArchive: true
        }
        success {
            echo "Deployment successful, API running on port 5050"
        }
        failure {
            echo "Deployment failed, result in logs"
        }
    }
}