pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/godhaniripal/PLANTIT.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t godhaniripal/tendergarden:latest .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if it exists
                    sh 'docker rm -f django-container || true'
                    // Run the new one
                    sh 'docker run -d -p 8000:8000 --name django-container godhaniripal/tendergarden:latest'
                }
            }
        }
    }
}
