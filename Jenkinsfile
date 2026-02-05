pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // building docker image and tagging docker image with jenkins build number
                sh 'docker build -t metrics-api:$BUILD_NUMBER .'
            }
        }
        stage('Test Application'){
            steps {
                // tee for archiving logs and pipefail for keeping exit code
                sh 'set -o pipefail; docker run --rm metrics-api:$BUILD_NUMBER sh -c "cd /api && python -m pytest tests" | tee test_log.log'
            }
        }
        stage('Deploy Application') {
            steps {
                // stopping exsisting containers
                sh 'docker stop metrics-container || true'
                sh 'docker rm metrics-container || true'
                //deploying new container with the image built previously
                sh 'docker run -d -p 5051:5050 --name metrics-container metrics-api:$BUILD_NUMBER python api/api/api.py'
            }
        }
    }  
    post {
        always {
            // archiving test logs regardless of result
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