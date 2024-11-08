# FastAPI Booking System

This project is a FastAPI-based booking system that includes a variety of features such as user authentication, hotel and room management, bookings, and more. The application is containerized using Docker and includes Prometheus monitoring and Grafana dashboards for metrics.

## Project Structure

```
.
├── Dockerfile
├── alembic.ini
├── app
│ ├── admin
│ │ ├── auth.py # Authentication for admin
│ │ └── views.py # Admin views
│ ├── bookings # Bookings app
│ ├── config.py # Configuration settings
│ ├── conftest.py # Test configuration
│ ├── dao
│ │ └── base.py # Base DAO class
│ ├── database.py # Database connection and setup
│ ├── exception.py # Custom exceptions
│ ├── hotels  # Hotels app
│ │ ├── rooms # Hotels Rooms app
│ ├── images # Images upload app
│ ├── logger.py # Logging configuration
│ ├── main.py # Application entry point
│ ├── migrations
│ │ ├── env.py # Alembic environment setup
│ │ ├── versions # Migrations files
│ ├── pages # Pages app
│ ├── prometheus # App with exceptions for testing prometheus
│ ├── tasks
│ │ ├── celery.py # Celery configuration
│ │ └── tasks.py # Background tasks
│ ├── templates
│ │ └── hotels.html # HTML template for hotels
│ ├── tests
│ │ ├── conftest.py # Test configuration
│ │ ├── fixtures_data # Mock data
│ │ ├── integration_tests # API integration tests
│ │ └── unit_tests # Unit tests
│ └── users # Users app
├── booking_infra
│ ├── docker-compose.yml # Docker Compose configuration
│ ├── grafana
│ │ └── grafana-dashboard.json # Grafana dashboard configuration
│ ├── nginx
│ │ └── nginx.conf # Nginx configuration
│ ├── postgres
│ │ └── init
│ │ └── 20-project.sh # Postgres initialization script
│ ├── prometheus
│ │ └── prometheus.yml # Prometheus configuration
│ └── rebuild_all_ins_db.sh # Script to rebuild infrastructure
├── fixtures
│ └── demo.sql # Demo SQL data
├── pyproject.toml # Project metadata and dependencies
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
└── scripts
├── entrypoint.sh # Entrypoint script for Docker
├── start_celery.sh # Script to start Celery worker
└── start_fastapi.sh # Script to start FastAPI app
```


## Setup

### Prerequisites
- Docker
- Docker Compose


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/web2cap/fastapi_introduce
   ```
2. Prepare .env
    ```bash
   cd fastapi-booking-system/booking_infra
   cp .env-local_example .env
   ```
3. Fill .env
4. Run docker:
    ```bash
    docker-compose up --build
    ```


## Docker Compose Configuration
The Docker Compose setup includes several services:

 - booking_pg: PostgreSQL database.
 - booking_redis: Redis for Celery.
 - booking_back: FastAPI application.
 - booking_celery: Celery worker.
 - booking_flower: Flower for Celery monitoring.
 - booking_nginx: Nginx for reverse proxy.
 - booking_prometheus: Prometheus for monitoring.
 - booking_grafana: Grafana for metrics visualization.

Networks and volumes are configured for inter-service communication and data persistence.

# Accessing the Application
 - API Documentation: http://localhost/v1/docs

 - Admin Interface: http://localhost/admin 

 - Celery Flower: http://localhost:5555

### Monitoring and Metrics


 - Grafana: http://localhost:3000 (default credentials: admin/admin)
 - Prometheus:  http://localhost:9090
