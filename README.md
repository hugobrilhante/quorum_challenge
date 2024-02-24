# Quorum Coding Challenge

🏛️ Working with legislative data

## Requirements

- Docker
- Node.js and npm

> Make sure you have these requirements installed on your system before running the script.


## How to Use


1. Execute the initialization script:

```
./start.sh
```

> This will run Docker Compose to set up the backend and start the npm server for the frontend.

2. Access the application:

Open a web browser and visit [http://localhost:3000](http://localhost:3000) to see the application in action.

## Run tests

```shell
cd backend
docker compose run --rm app python manage.py test
```

## Project Structure

- `backend/`: Contains an application using django 
- `frontend/`: Contains an application using nextjs
- `start.sh`: Initialization script that automates the execution of Docker Compose and npm.

