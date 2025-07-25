variable "aws_region" {
  default = "us-east-1"
}

variable "ecs_cluster_name" {
  default = "flask-ecs-cluster"
}

variable "docker_image" {
  default = "srisaisiddhartha/flask-ecs-project:latest"
}
