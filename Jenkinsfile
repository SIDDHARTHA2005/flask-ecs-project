pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        TF_VAR_docker_image = "srisaisiddhartha/flask-ecs-project:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set up Terraform') {
            steps {
                sh 'terraform init'
            }
        }

        stage('Validate Terraform') {
            steps {
                sh 'terraform validate'
            }
        }

        stage('Plan Infrastructure') {
            steps {
                sh 'terraform plan -out=tfplan'
            }
        }

        stage('Apply Infrastructure') {
            steps {
                sh 'terraform apply -auto-approve tfplan'
            }
        }
    }
}
