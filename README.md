# Project1

# Project1 - LLM Automation Agent API

## Overview
Project1 is an LLM-powered Automation Agent designed to execute various deterministic tasks. The application is containerized using Docker and exposes a REST API for task execution.

## Features
- Executes predefined operational and business tasks
- Provides a REST API with FastAPI
- Containerized using Docker
- Handles tasks such as:
  - Formatting Markdown files
  - Counting Wednesdays in a file
  - Sorting contact lists
  - Fetching recent log entries

## Installation & Setup
### Prerequisites
- Install **Docker**: [Download Here](https://www.docker.com/get-started)
- Install **Python 3.12**: [Download Here](https://www.python.org/downloads/)

### Clone the Repository
```sh
git clone https://github.com/22f3001203/Project1.git
cd Project1
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application
### Run Locally
```sh
python -m app.main
```

### Run with Docker
#### Build the Docker Image
```sh
docker build -t sonidhriti/project1 .
```

#### Run the Docker Container
```sh
docker run -p 8000:8000 sonidhriti/project1
```

### API Endpoints
Once running, access the API at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Run Task**:
  ```sh
  curl -X 'POST' \
    'http://127.0.0.1:8000/run?task=count%20wednesdays' \
    -H 'accept: application/json'
  ```

## Pushing the Docker Image to Docker Hub
If you want to share your Docker image:
```sh
docker login
docker push sonidhriti/project1
```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to GitHub (`git push origin feature-branch`)
5. Create a Pull Request

## License
This project is licensed under the **MIT License**.

