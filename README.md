# Production-Style Three-Tier Flask Application (Docker + Nginx + MySQL)

## 📌 Overview
  This project demonstrates a production-style containerized web application built using a three-tier architecture:
  
  **Client → Nginx → Gunicorn (Flask) → MySQL**

  The system is orchestrated using Docker Compose and designed with production best practices including reverse proxy configuration, 
  service-based networking, environment isolation, and health checks.
  
---
## 🏗 Architecture

- **Web Tier:** Nginx (Reverse Proxy)  
- **Application Tier:** Flask served via Gunicorn  
- **Database Tier:** MySQL 8.0 with persistent volume  
- **Orchestration:** Docker Compose  
- **Future CI/CD:** Jenkins + Trivy (planned)
  
  --- 
## 🚀 Features
 - Reverse proxy using Nginx
 - Gunicorn production WSGI server
 - MySQL persistent storage using Docker volumes
 - Environment variable–based configuration
 - Docker internal DNS communication
 - Health check with service dependency
 - Secure configuration via .env (excluded from Git)
 
---
## 📂 Project Structure
 .
 ├── app/
 ├── nginx/
 ├── Dockerfile
 ├── docker-compose.yml
 ├── .dockerignore
 └── README.md
 
---
## 🛠 How to Run Locally

1. Create a `.env` file with required variables.  
2. Build and start containers:
     ' docker compose up --build '
3.  Access application: 
     ' http://localhost '
    
---
## 🔐 Security Practices
  - .env excluded from Git
  - .env excluded from Docker build context
  - MySQL not exposed publicly
  - Internal container networking
  - Planned image vulnerability scanning using Trivy
  
---
## 🔄 Roadmap
  - Jenkins CI/CD pipeline
  - Docker image vulnerability scanning with Trivy
  - Automated image push to Docker Hub / AWS ECR
  - EC2 provisioning via Ansible
  - Future project: Kubernetes + ArgoCD GitOps deployment
---

## 🚀 DevOps Automation (Phase 2)

Infrastructure provisioning and CI/CD automation for this project is implemented in a separate repository:

👉 [two-tier-devops-infra](LINK_HERE)

Includes:
- Ansible-based EC2 provisioning
- Jenkins automation
- Trivy vulnerability scanning
- Docker image build & push pipeline
