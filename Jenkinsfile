pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mdmaaz304/devops_assignment2-app:latest"
    }

    stages {

        stage('Checkout Project Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mdmaaz304/devops_assignment2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}", "./app")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-cred') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                set KUBECONFIG=C:/Users/user/.kube/config
                kubectl apply -f k8s\\deployment.yaml
                kubectl apply -f k8s\\service.yaml
                '''
            }
        }
    }
}
