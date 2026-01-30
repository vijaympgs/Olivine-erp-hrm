resource "aws_ecs_cluster" "olivine" {
  name = "olivine-ecs-cluster"
}

resource "aws_ecs_task_definition" "backend" {
  family                   = "olivine-backend"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 512
  memory                   = 1024
  network_mode             = "awsvpc"
}
