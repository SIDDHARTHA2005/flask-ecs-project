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
                bat 'terraform init'
            }
        }

        stage('Validate Terraform') {
            steps {
                bat 'terraform validate'
            }
        }

        stage('Plan Infrastructure') {
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
            }
            steps {
                bat 'terraform plan -out=tfplan'
            }
        }

        stage('Apply Infrastructure') {
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
            }
            steps {
                bat 'terraform apply -auto-approve tfplan'
            }
        }
    }
}
