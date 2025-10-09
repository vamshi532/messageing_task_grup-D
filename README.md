# Messaging System using Flask, Celery, and RabbitMQ

## Project Overview
This project is a simple messaging system built using Flask, Celery, and RabbitMQ.  
It demonstrates how asynchronous background processing works in web applications.  
The system uses Celery workers to handle background tasks such as sending emails,  
while RabbitMQ acts as the message broker for communication between Flask and Celery.

---

## Technologies Used
- Python 3.10 or above  
- Flask for the web server  
- Celery for background task management  
- RabbitMQ as the message broker  
- Docker and Docker Compose for containerization

---

## Project Structure
messaging-system/  
│  
├── app.py               Flask application that sends tasks  
├── tasks.py             Celery worker that processes tasks  
├── Dockerfile           Builds the Flask container  
├── docker-compose.yml   Defines all containers and services  
├── requirements.txt     List of dependencies  
├── .env                 Environment variables file (for email credentials)  
└── README.md            Documentation  

---

## How the System Works
1. The Flask web server exposes an endpoint `/send-email` that creates a Celery task.  
2. Celery sends the task to RabbitMQ, which acts as a message broker.  
3. RabbitMQ stores the task in a queue using FIFO (First In, First Out) order.  
4. The Celery worker picks up the task and processes it asynchronously.  
5. The email is then sent to the configured receiver.

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <your-repo-link>
cd messaging-system
