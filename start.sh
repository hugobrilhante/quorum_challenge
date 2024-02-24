#!/bin/bash

# Function to run Docker Compose in the backend folder
run_docker_compose() {
    cd backend || exit 1
    docker-compose up -d
    cd ..
}

# Function to run npm run dev in the frontend folder
run_npm_dev() {
    cd frontend || exit 1
    npm run dev
    cd ..
}

# Run Docker Compose in the backend folder
run_docker_compose

# Run npm run dev in the frontend folder
run_npm_dev

