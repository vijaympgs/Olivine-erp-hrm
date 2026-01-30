# AWS / GCP Migration Blueprint

## Phase 1: Lift & Shift
- Dockerize backend
- Externalize Postgres
- Use S3 / GCS for media

## Phase 2: Managed Services
AWS:
- ECS / EKS
- RDS PostgreSQL
- ALB + ACM

GCP:
- Cloud Run
- Cloud SQL
- Cloud Load Balancer

## Phase 3: Scale
- Redis caching
- Background workers
- Centralized logging
